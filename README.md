# Raspberry Pi Pico fuel level sensor

## Purpose

- Measuring level of heating oil (diesel) inside a polypropelyne storage tank

## Process

- Fuel storage system consists of 6 identical tanks
- Tanks are approximately rectangular
- Fuel is equally distributed between the 6 tanks, so the fuel levels are identical
- Volume of fuel remaining can be calcalated by knowing the height of the fuel
- The sensor measures the distance between the fuel level and the sensor height, which is known
- This version includes both ultrasonic and laser-based measures to figure out which is most accurate
- Pi Pico runs the Microdot HTTP server, and responds to GET requests to `/laser` and `/ultrasonic` with the distance between sensor and fuel in mm

## TODO
- add code to adjust for sensor accuracy and mounting height
- add sketches for hardware enclosure
- add some diagnostics for eventual integration with Home Assistant

## Software BOM
- Micropython
- Microdot HTTP library

## Hardware BOM
- Raspberry Pi Pico W
- VL53LOX time-of-flight sensor
- HCSR04 ultrasonic distance sensor

## Circuit diagram
![breadboard diagram](/docs//tank_sensor_breadboard.png?raw=true "Breadboard layout")