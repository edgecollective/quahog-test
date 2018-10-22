import gc

from machine import Pin
from machine import SPI
from upy_rfm9x import RFM9x
from machine import I2C
import ssd1306
import time


TIMEOUT = 2
DISPLAY = True
OLED_LINESKIP=18
OLED_CURRENTLINE=0

# i2c (and display) tests
i2c = I2C(-1, Pin(14), Pin(2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.text("awake!",0,OLED_CURRENTLINE)
oled.show()

time.sleep(TIMEOUT)

oled.text("sleeping...",0,30)
oled.show()

done=Pin(19,Pin.OUT)
done.value(False)
done.value(True)
#time.sleep(.1)
done.value(False)


