import time
from machine import Pin, I2C
from vl53l0x import VL53L0X

def measure():

    id = 0
    sda = Pin(20)
    scl = Pin(21)

    i2c = I2C(id=id, sda=sda, scl=scl)

    print(i2c.scan())
    tof = VL53L0X(i2c)

    budget = tof.measurement_timing_budget_us
    tof.set_measurement_timing_budget(40000)

    tof.set_Vcsel_pulse_period(tof.vcsel_period_type[0], 12)
    tof.set_Vcsel_pulse_period(tof.vcsel_period_type[1], 8)

    sum_readings = 0
    valid_readings = 0

    for count in range(10):
        dist = tof.ping()
        if dist != 8191: # ignore failed reading
            sum_readings += dist
            valid_readings += 1
        time.sleep_ms(100)  # Short delay of 0.1 seconds to reduce CPU usage

    average = sum_readings / valid_readings
    return average

def l_read_tank_depth():

    average = measure()

    print("Frickin' lasers...")
    print(f"average {average}")
    return average

