import gc

from machine import Pin
from machine import SPI
from upy_rfm9x import RFM9x
from machine import I2C
import ssd1306

TIMEOUT = 5
DISPLAY = True
OLED_LINESKIP=18
OLED_CURRENTLINE=0

# i2c (and display) tests
i2c = I2C(-1, Pin(14), Pin(2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.text("i2c works;",0,OLED_CURRENTLINE)
oled.show()

# radio test
sck=Pin(25)
mosi=Pin(33)
miso=Pin(32)
cs = Pin(26, Pin.OUT)
#reset=Pin(13)
led = Pin(13,Pin.OUT)

resetNum=27

spi=SPI(1,baudrate=5000000,sck=sck,mosi=mosi,miso=miso)

rfm9x = RFM9x(spi, cs, resetNum, 915.0)

OLED_CURRENTLINE=OLED_CURRENTLINE+OLED_LINESKIP
oled.text("Radio works;",0,OLED_CURRENTLINE)
oled.show()



# wrap up
OLED_CURRENTLINE=OLED_CURRENTLINE+OLED_LINESKIP
oled.text("... oh, yeah.",0,OLED_CURRENTLINE)
oled.show()

