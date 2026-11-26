try:
    import usocket as socket
except:
    import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'AcademiasIndetec'
password = 'Indetec_2026'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Conexion exitosa')
print(station.ifconfig())
