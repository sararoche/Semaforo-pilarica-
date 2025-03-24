# main.py -- put your code here!
from machine import Pin, ADC
from time import sleep
from machine import mem32

peatonal1verde=Pin(23,Pin.OUT)
peatonal2verde=Pin(22,Pin.OUT)
vehicular1amarillo=Pin(21,Pin.OUT)
vehicular2amarillo=Pin(19,Pin.OUT)
vehicular1verde=Pin(18,Pin.OUT)
vehicular2verde=Pin(5,Pin.OUT)
peatonal1rojo=Pin(13,Pin.OUT)
peatonal2rojo=Pin(12,Pin.OUT)
vehicular3amarillo=Pin(14,Pin.OUT)
vehicular1rojo=Pin(27,Pin.OUT)
vehicular2rojo=Pin(26,Pin.OUT)
vehicular3rojo=Pin(25,Pin.OUT)
vehicular3verde=Pin(16,Pin.OUT)

global b_pare
global b_temperatura

b_pare=False
b_temperatura=False

lm35_Pin=ADC(Pin(32))
lm35_Pin.atten(ADC.ATTN_11DB)
lm35_Pin.width(ADC.WIDTH_10BIT)


def off():
   for luz in [peatonal1verde,peatonal2verde,vehicular3verde,vehicular1verde,vehicular2verde,peatonal1rojo,peatonal2rojo,vehicular1amarillo,vehicular2amarillo,vehicular3amarillo,vehicular1rojo,vehicular2rojo,vehicular3rojo]:
        luz.off()
        luz.value(0)


def leer_temperatura():
    valor_temperatura=lm35_Pin.read()
    voltaje=(valor_temperatura/1023.0)*3.3
    temperatura_c=voltaje*100
    print("La temperatura es: ",round(temperatura_c,2),"grados Celsius")
    return temperatura_c

def interrupcion_temperatura(Pin):
    global b_temperatura
    print("lectura de temperatura")
    b_temperatura=not b_temperatura

def interrupcion_pare(Pin):
    global b_pare
    print("Entre a la funcion interrupcion")
    b_pare=True


pare=Pin(33,Pin.IN,Pin.PULL_UP)
pare.irq(trigger=Pin.IRQ_FALLING, handler=interrupcion_pare)

temperatura=Pin(17,Pin.IN,Pin.PULL_UP)
temperatura.irq(trigger=Pin.IRQ_FALLING, handler=interrupcion_temperatura)

GPIO_SET=const(0x3FF44004)

