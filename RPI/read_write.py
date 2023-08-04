from machine import Pin, UART, ADC
import time

uart = UART(0, 57600)

sensor = ADC(Pin(26))
level=0
boucle=0

while True:
    
    if uart.any() > 0 :
        level = uart.read()
        level = str(level)
        level = level[2]
        if level == "1" :
            print("Niveau 1")
        elif level =="2" :
            print("Niveau 2")
        elif level == "3" :
            print("Niveau 3")
        else :
            print("error")
        
    val_sensor = sensor.read_u16()
    simply_val_sensor = round(val_sensor/100)
    uart.write(str(simply_val_sensor))
    time.sleep(1)