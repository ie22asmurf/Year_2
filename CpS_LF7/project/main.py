import machine
import dht
from ssd1306 import SSD1306_I2C
import utime
# Bibliotheken laden
from machine import Pin
from time import sleep
# Initialisierung von GPIO13 als Ausgang
led = Pin(13, Pin.OUT)


# Datenpin initialisieren
dataPin = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_UP)
#I2C initialisieren
i2c_dev = machine.I2C(1, scl=machine.Pin(27), sda=machine.Pin(26), freq=200000)

#Sensor (DHT22) initialisieren
sensor = dht.DHT22(dataPin)
#Display initialisieren
oled = SSD1306_I2C(128, 64, i2c_dev)
# Sensor messen lassen
sensor.measure()
# Messwerte ausgeben
print(sensor.temperature())
print(sensor.humidity())
zustand = ""
oled.text("Starte Messungen",0,0)
oled.show()
utime.sleep(1)
while True:
    #Display leeren und mit neuer Temperatur befüllen
    oled.fill(0)
    sensor.measure()
    temperatur = sensor.temperature()
    ausgabe_1 = "" + str(temperatur) +" C"    
    oled.text(ausgabe_1,0,0)
    oled.text(zustand,0,20)
    oled.show()
    if (temperatur < 25):
        zustand = "ok"
        #Grünes LED aktivieren
        led = Pin(13, Pin.OUT)
        led.on()
        sleep(5)
        led.off()
    elif (temperatur < 30):
        zustand = "50 %"
        #Gelbes LED aktivieren
        led = Pin(12, Pin.OUT)
        led.on()
        sleep(5)
        led.off()
    else :
        zustand = "100 %"
        #Rotes LED aktivieren
        led = Pin(11, Pin.OUT)
        led.on()
        sleep(5)
        led.off()
utime.sleep(1)