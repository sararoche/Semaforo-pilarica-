from machine import Pin, ADC
from time import sleep
from machine import mem32

# Definir los pines de los LEDs
peatonal1verde = Pin(23, Pin.OUT)
peatonal2verde = Pin(22, Pin.OUT)
peatonal3verde = Pin(21, Pin.OUT)
vehicular4amarillo = Pin(19, Pin.OUT)
vehicular5verde = Pin(18, Pin.OUT)
vehicular6verde = Pin(5, Pin.OUT)
peatonal1rojo = Pin(13, Pin.OUT)
peatonal2rojo = Pin(12, Pin.OUT)
peatonal3rojo = Pin(14, Pin.OUT)
vehicular4rojo = Pin(27, Pin.OUT)
vehicular5rojo = Pin(26, Pin.OUT)
vehicular6rojo = Pin(25, Pin.OUT)

# Variables globales
global b_pare
global b_temperatura
b_pare = False
b_temperatura = False

# Sensor de temperatura
lm35_Pin = ADC(Pin(32))
lm35_Pin.atten(ADC.ATTN_11DB)
lm35_Pin.width(ADC.WIDTH_10BIT)

def off():
    for luz in [peatonal1verde, peatonal2verde, peatonal3verde, vehicular4amarillo, vehicular5verde, vehicular6verde,
                peatonal1rojo, peatonal2rojo, peatonal3rojo, vehicular4rojo, vehicular5rojo, vehicular6rojo]:
        luz.off()

def leer_temperatura():
    valor_temperatura = lm35_Pin.read()
    voltaje = (valor_temperatura / 1023.0) * 3.3
    temperatura_c = voltaje * 100
    print("La temperatura es:", round(temperatura_c, 2), "grados Celsius")
    return temperatura_c

def interrupcion_temperatura(Pin):
    global b_temperatura
    print("Lectura de temperatura")
    b_temperatura = not b_temperatura

def interrupcion_pare(Pin):
    global b_pare
    print("Interrupción activada: Pare")
    b_pare = True

# Configurar los botones
pare = Pin(33, Pin.IN, Pin.PULL_UP)
pare.irq(trigger=Pin.IRQ_FALLING, handler=interrupcion_pare)

temperatura = Pin(17, Pin.IN, Pin.PULL_UP)
temperatura.irq(trigger=Pin.IRQ_FALLING, handler=interrupcion_temperatura)

GPIO_SET = const(0x3FF44004)

# Ciclo principal
while True:
    if b_temperatura:
        off()
        leer_temperatura()
        sleep(1)
    else:
        mem32[GPIO_SET] = 0b00010010011000110000000000000
        sleep(6.8)
        mem32[GPIO_SET] = 0b00010000010000110000000000000
        sleep(0.5)
        mem32[GPIO_SET] = 0b00010010011000110000000000000
        sleep(0.5)
        mem32[GPIO_SET] = 0b00010000010000110000000000000
        sleep(0.3)
        mem32[GPIO_SET] = 0b00010010011000110000000000000
        sleep(0.3)
        mem32[GPIO_SET] = 0b00010000010000110000000000000
        sleep(0.2)
        mem32[GPIO_SET] = 0b00010010011000110000000000000
        sleep(0.2)
        mem32[GPIO_SET] = 0b00010000010000110000000000000
        sleep(0.1)
        mem32[GPIO_SET] = 0b00010010011000110000000000000
        sleep(0.1)
        mem32[GPIO_SET] = 0b00100100010000101000000100000
        sleep(6.8)
        mem32[GPIO_SET] = 0b00100000000000101000000000000
        sleep(0.5)
        mem32[GPIO_SET] = 0b00100100010000101000000100000
        sleep(0.5)
        mem32[GPIO_SET] = 0b00100000000000101000000000000
        sleep(0.3)
        mem32[GPIO_SET] = 0b00100100010000101000000100000
        sleep(0.3)
        mem32[GPIO_SET] = 0b00100000000000101000000000000
        sleep(0.2)
        mem32[GPIO_SET] = 0b00100100010000101000000100000
        sleep(0.2)
        mem32[GPIO_SET] = 0b00100000000000101000000000000
        sleep(0.1)
        mem32[GPIO_SET] = 0b00100100010000101000000100000
        sleep(0.1)

        if b_pare:
            mem32[GPIO_SET] = 0b01110111000000000000000000000
            sleep(4.8)
            mem32[GPIO_SET] = 0b01110000000000000000000000000
            sleep(0.5)
            mem32[GPIO_SET] = 0b01110111000000000000000000000
            sleep(0.5)
            mem32[GPIO_SET] = 0b01110000000000000000000000000
            sleep(0.3)
            mem32[GPIO_SET] = 0b01110111000000000000000000000
            sleep(0.3)
            mem32[GPIO_SET] = 0b01110000000000000000000000000
            sleep(0.2)
            mem32[GPIO_SET] = 0b01110111000000000000000000000
            sleep(0.2)
            mem32[GPIO_SET] = 0b01110000000000000000000000000
            sleep(0.1)
            mem32[GPIO_SET] = 0b01110111000000000000000000000
            sleep(0.1)
            b_pare = 0