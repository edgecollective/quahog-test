sudo python venv/lib/python2.7/site-packages/esptool.py --port /dev/ttyUSB0 erase_flash
sudo python venv/lib/python2.7/site-packages/esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20180821-v1.9.4-479-g828f771e3.bin 
