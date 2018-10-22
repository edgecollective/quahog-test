import ujson as json
import urequests as requests
import time
import dht
import machine
from machine import Pin
from machine import SPI
import ssd1306
from machine import I2C
from upy_rfm9x import RFM9x

TIMEOUT = .2
import time

#radio
sck=Pin(25)
mosi=Pin(33)
miso=Pin(32)
cs = Pin(26, Pin.OUT)
resetNum=27
spi=SPI(1,baudrate=5000000,sck=sck,mosi=mosi,miso=miso)
rfm9x = RFM9x(spi, cs, resetNum, 915.0)

# set up the display
i2c = I2C(-1, Pin(14), Pin(2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# set up the 'done' pin
done_pin=Pin(22,Pin.OUT)
done_pin.value(0)

# indicate that we're starting up
oled.fill(0)
oled.text("Starting up ...",0,0)
oled.show()

# set up the DHT22 temp + humidity sensor
d = dht.DHT22(machine.Pin(18))

# set up FARMOS params
base_url='https://wolfesneck.farmos.net/farm/sensor/listener/'
public_key='054d3116a74fae5dd36550013d50c848'
private_key='014d3116a74fae5dd36550013d50c848'
url = base_url+public_key+'?private_key='+private_key
headers = {'Content-type':'application/json', 'Accept':'application/json'}

# wifi parameters
#WIFI_NET = 'Artisan\'s Asylum'
#WIFI_PASSWORD = 'I won\'t download stuff that will get us in legal trouble.'

WIFI_NET = 'Dennis Village Mercantile'
WIFI_PASSWORD = 'jimmytuna'

# function for posting data
def post_data():
    try:
        r = requests.post(url,data=json.dumps(payload),headers=headers)
    except Exception as e:
        print(e)
        #r.close()
        return "timeout"
    else:
        r.close()
        print('Status', r.status_code)
        return "posted"

# function for connecting to wifi
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)	
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(False)
        sta_if.active(True)
        sta_if.connect(WIFI_NET, WIFI_PASSWORD)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

index=0

# main loop
while True:
    # make measurements
    rfm9x.receive(timeout=TIMEOUT)

    if rfm9x.packet is not None:
        print(rfm9x.packet)
        try:
            txt=str(rfm9x.packet,'ascii')
            print(txt.split(","))
            items=txt.split(",")
            if len(items)==5:
                count=items[0]
                batt=float(items[1])/100.
                light=int(items[2])
                temp_1=float(items[3])/100.
                temp_2=float(items[4])/100.
            #print(count,batt,light,temp_1,temp_2)
            #oled.fill(0)
            #oled.text(str(count),0,0)
            #oled.show()
                
        except Exception as e:
            print(e)    
