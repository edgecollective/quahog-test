import gc

from machine import Pin
from machine import SPI
from upy_rfm9x import RFM9x
from machine import I2C
import ssd1306

i2c = I2C(-1, Pin(14), Pin(2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.text("-- Screen works (obvi) ...",0,0)
oled.show()

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

oled.text("-- Radio works ...",0,20)
oled.show()

# wrap up
oled.text("... oh, yeah.",0,50)
oled.show()

