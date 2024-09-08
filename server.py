import json
import time
import network
import machine
import uasyncio as asyncio
from asyncio import gather
from microdot import Microdot, Response

from laser import l_read_tank_depth
from ultrasound import us_read_tank_depth

WIFI_SSID = 'zuercherstrasse'
WIFI_PASSWORD = 'c4rs1ckv13wr04d'

app = Microdot()

### SERVER
@app.route('/laser', methods=['GET'])
async def root(request):
    dist = l_read_tank_depth()
    print(f"GET / : distance = {dist}")
    data = {
        "type": "laser",
        "distance": dist
    }
    return json.dumps(data), 200, {'Content-Type': 'application/json'}

@app.route('/ultrasound', methods=['GET'])
async def root(request):
    dist = us_read_tank_depth()
    print(f"GET / : distance = {dist}")
    data = {
        "type": "ultrasound",
        "distance": dist
    }
    return json.dumps(data), 200, {'Content-Type': 'application/json'}

@app.errorhandler(404)
async def not_found(request):
    return {'error': 'resource not found'}, 404

### NETWORK

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
        
def start_server():
    print('Starting server on port 80...')
    try:
        app.run(port=80)
        print('Server started on port 80')
    except:
        app.shutdown()

try:
    connect()
except KeyboardInterrupt:
    machine.reset()

start_server()
