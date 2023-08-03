from machine import Pin, UART, ADC
import time

uart = UART(0, 57600)

sensor = ADC(Pin(26))
test=0
boucle=0

while True:
    
    if uart.any() > 0 :
        test = uart.read()
        test = str(test)
        print(test)
        boucle=boucle+1
        print(boucle)
    val_sensor = sensor.read_u16()
    simply_val_sensor = round(val_sensor/100)
    uart.write(str(simply_val_sensor))
    print(simply_val_sensor)
    time.sleep(5)