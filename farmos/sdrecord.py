import ujson as json
import urequests as requests
import time
import dht
import machine
from machine import Pin
from machine import SPI
import ssd1306
from machine import I2C
import sdcard
import os

i2c = I2C(-1, Pin(14), Pin(2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

done_pin=Pin(22,Pin.OUT)
#done_pin.value(0)

oled.fill(0)
oled.text("Starting up ...",0,0)
oled.show()

d = dht.DHT22(machine.Pin(18))

oled.text("Measuring...",0,20)
oled.show()

d.measure()
t=d.temperature()
h=d.humidity()

sck=Pin(16)
mosi=Pin(4)
miso=Pin(17)
cs = Pin(15, Pin.OUT)
spi2=SPI(2,baudrate=5000000,sck=sck,mosi=mosi,miso=miso)

oled.text("Writing...",0,30)
oled.show()

sd = sdcard.SDCard(spi2, cs)
os.mount(sd,'/sd')

f=open('/sd/test.csv','a')

f.write(str(t)+','+str(h)+'\n')
f.close()

time.sleep(3)

oled.text("Sleeping...",0,50)
oled.show()

done_pin.value(1)
machine.deepsleep()

