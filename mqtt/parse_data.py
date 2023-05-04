import dashboard
import random

# Parse 16 bit bytes to available data for influxdb

async def parse_data(data):
    '''
        example data: data = b'\x01\x08\x01\x03\x03\x00\x01\x00\x00\x04\x08\x01\t\x00\x02\x04\x03\x17\x14' 
    '''
    data = list(data)
    dashboard_id = ''.join(map(str, data[:8]))
    if dashboard_id == '18133010':
        # mybashboard = dashboard.dashboard_1()
        # mybashboard.speed = data[11]
        # mybashboard.temperature = data[12]
        # mybashboard.pressure_1 = data[13]
        # mybashboard.pressure_2 = data[14]
        # mybashboard.battery_voltage = data[16]
        # mybashboard.soc_1 = data[17]
        # mybashboard.soc_2 = data[18]

        # generate random data for test
        mybashboard = dashboard.dashboard_1()
        mybashboard.speed = random.randint(0,255)
        mybashboard.temperature = random.randint(0,255)
        mybashboard.pressure_1 = random.randint(0,255)
        mybashboard.pressure_2 = random.randint(0,255)
        mybashboard.battery_voltage = random.randint(0,255)
        mybashboard.soc_1 = random.randint(0,1)
        mybashboard.soc_2 = random.randint(0,1)
        fields = {
                    'speed' : mybashboard.speed,
                    'temperature' : mybashboard.temperature,
                    'pressure_1' : mybashboard.pressure_1,
                    'pressure_2' : mybashboard.pressure_2,
                    'battery_voltage' : mybashboard.battery_voltage,
                    'soc_1' : mybashboard.soc_1,
                    'soc_2' : mybashboard.soc_2
        } 
        print(fields)
        return fields

if __name__ == '__main__':
    data = b'\x01\x08\x01\x03\x03\x00\x01\x00\x00\x04\x08\x01\t\x00\x02\x04\x03\x17\x14'
    parse_data(data)


