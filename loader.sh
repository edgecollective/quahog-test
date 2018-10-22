python ./esptool.py --port /dev/ttyUSB0 erase_flash
python ./esptool.py esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 *.bin
