import usocket as socket
import network
from machine import Pin
import dht

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'ssid'
password = 'passwd'
ap=network.WLAN(network.AP_IF)
ap.active(False)
station = network.WLAN(network.STA_IF)
station.active(True)
#station.ifconfig(config=('192.168.1.2','255.255.255.0','192.168.1.1','8.8.8.8'))
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

sensor = dht.DHT11(Pin(2))
