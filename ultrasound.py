import time
import machine

# Define pin numbers for ultrasonic sensor's TRIG and ECHO pins
TRIG = machine.Pin(17, machine.Pin.OUT)  # TRIG pin set as output
ECHO = machine.Pin(16, machine.Pin.IN)  # ECHO pin set as input

### TANK
def us_read_distance():
    TRIG.low()  # Set TRIG low
    time.sleep_us(2)  # Wait for 2 microseconds
    TRIG.high()  # Set TRIG high
    time.sleep_us(10)  # Wait for 10 microseconds
    TRIG.low()  # Set TRIG low again

    while not ECHO.value():
        pass

    time1 = time.ticks_us()  # Record time when ECHO goes high

    # Wait for ECHO pin to go low
    while ECHO.value():
        pass

    time2 = time.ticks_us()  # Record time when ECHO goes low

    # Calculate the duration of the ECHO pin being high
    during = time.ticks_diff(time2, time1)

    # Return the calculated distance (using speed of sound)
    return during * 340 / 2 / 10000  # Distance in centimeters

def us_read_tank_depth():

    sum_readings = 0
    
    for count in range(5):
        dist = us_read_distance()
        sum_readings += dist

    # Calculate and return the average
    average = sum_readings / 5
    print("Ultrasound")
    print(f"average {average}")
    return average
