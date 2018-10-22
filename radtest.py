import gc

from machine import Pin
from machine import SPI

from upy_rfm9x import RFM9x

TIMEOUT = 5
DISPLAY = True


sck=Pin(25)
mosi=Pin(33)
miso=Pin(32)
cs = Pin(26, Pin.OUT)
#reset=Pin(13)
led = Pin(13,Pin.OUT)

resetNum=27

spi=SPI(1,baudrate=5000000,sck=sck,mosi=mosi,miso=miso)

rfm9x = RFM9x(spi, cs, resetNum, 915.0)
