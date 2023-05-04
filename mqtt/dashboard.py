# Function: dashboard class

class dashboard_1:
    '''
        speed           车速            float 0-255
        temperature     温度            float 0-255
        pressure_1      压力1           float 0-255
        pressure_2      压力2           float 0-255
        driver_flow_1   驱动器流量计1    float 0-255
        driver_flow_2   驱动器流量计2    float 0-255
        driver_flow_3   驱动器流量计3    float 0-255
        driver_flow_4   驱动器流量计4    float 0-255    
        driver_flow_id  驱动器流量计ID   float 0-255
        battery_voltage 蓄电瓶电压       float 0-255
        soc_1           SOC1            float 0-255  
        soc_2           SOC2            float 0-255 
    '''
    def __init__(   self, speed=0, temperature=0, pressure_1=0, pressure_2=0,
                    driver_flow_1=0, driver_flow_2=0, driver_flow_3=0, driver_flow_4=0, driver_flow_id=0,
                    battery_voltage=0, soc_1=0, soc_2=0
        ):
        self.id = '18133010'
        self.speed = speed
        self.temperature = temperature
        self.pressure_1 = pressure_1
        self.pressure_2 = pressure_2
        self.driver_flow_1 = driver_flow_1
        self.driver_flow_2 = driver_flow_2
        self.driver_flow_3 = driver_flow_3
        self.driver_flow_4 = driver_flow_4
        self.driver_flow_id = driver_flow_id
        self.battery_voltage = battery_voltage
        self.soc_1 = soc_1
        self.soc_2 = soc_2
    


