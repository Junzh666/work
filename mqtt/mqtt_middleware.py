import asyncio
import asyncio_mqtt as aiomqtt
import random
import paho.mqtt as mqtt
from parse_data import parse_data
from datetime import datetime
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import ASYNCHRONOUS
from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync


# ENV for mqtt and influxdb
MQTT_TOPIC = "test/******"
MQTT_SERVER = "localhost"
MQTT_PORT = 1883
MQTT_MEASUREMENT = "mqtt_consumer"
MQTT_FIELD = "message"
INFLUXDB_SERVER = "******"
INFLUXDB_PORT = 8086
INFLUXDB_ORG = "******"
INFLUXDB_BUCKET = "******"
INFLUXDB_TOKEN = "******"

with open('test.txt', 'r') as f:
	topics = [ i.strip() for i in f.readlines() ]

async def write_influxdb(measurement, tags, fields):
    # create influxdb point
    point = {
        "measurement": measurement,
        "time": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
        "tags": tags,
        "fields": fields
    }
    # write point to influxdb
    async with InfluxDBClientAsync(
        url=f"http://{INFLUXDB_SERVER}:{INFLUXDB_PORT}", token=INFLUXDB_TOKEN, org=INFLUXDB_ORG
    ) as influxdb_client:
        await influxdb_client.write_api().write(bucket=INFLUXDB_BUCKET, record=point)

async def main():
    async with aiomqtt.Client(hostname="localhost", port=1883) as client:
        async with client.messages() as messages:
            await client.subscribe(MQTT_TOPIC)
            async for message in messages:
                data = message.payload
                data = b'\x01\x08\x01\x03\x03\x00\x01\x00\x00\x04\x08\x01\t\x00\x02\x04\x03\x17\x14'
                myfields = await parse_data(data)
                tags = {'topic': random.choice(topics) }
                # write data to influxdb
                await write_influxdb(
                    MQTT_MEASUREMENT,
                    tags,
                    myfields
                )

if __name__ == '__main__':
    asyncio.run(main())
