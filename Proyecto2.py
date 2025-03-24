# Pines de los LEDs
luces_semaforos = [2, 4, 5, 15, 13, 21, 18, 19, 22, 23]
bandera = 0
peatonal_activado = False

def accion(pin):
    global bandera, peatonal_activado
    # Debounce simple
    sleep(0.1)
    if pin.value():  # Verifica si el botón sigue presionado
        bandera = 1
        peatonal_activado = True  # Activa el cruce peatonal

# Inicializar el pulsador
pulsador = Pin(26, Pin.IN)
pulsador.irq(trigger=Pin.IRQ_RISING, handler=accion)
GPIO_OUT_REG = const(0x03FF44004)

# Activar los pines de la carrera y de la calle
for i in range(10):
    Pin(luces_semaforos[i], Pin.OUT)

# Ciclo para el semáforo
while True:
    if bandera == 1 and peatonal_activado:
        print("Activando cruce peatonal...")
        # Vehicular en rojo y peatonal en verde
        mem32[GPIO_OUT_REG] = 0b00000000101000001010000000000000  # Solo peatonal en verde
        sleep(8)  # Tiempo que los peatones cruzan
        peatonal_activado = False
        bandera = 0  # Restablece la bandera para volver al ciclo normal
        print("Ciclo normal retomado.")
    else:
        print("Semáforo funcionando normalmente.")
        # Ciclo normal del semáforo
        # Carrera: ROJO vehicular y VERDE peatonal
        mem32[GPIO_OUT_REG] = 0b00000000100000000010000000110000
        sleep(3)  # Tiempo fijo
        # Titila VERDE peatonal
        for _ in range(4):
            mem32[GPIO_OUT_REG] ^= 0b00000000000000000010000000100000
            sleep(0.5)
        # Carrera: AMARILLO vehicular encendido y ROJO peatonal
        mem32[GPIO_OUT_REG] = 0b00000000000001000000000000010100
        sleep(1)  # Tiempo fijo
        # Carrera: ROJO peatonal y vehicular
        mem32[GPIO_OUT_REG] = 0b00000000011010001000000000000000
        sleep(3)  # Tiempo fijo
        # Titila VERDE peatonal
        for _ in range(4):
            mem32[GPIO_OUT_REG] ^= 0b00000000010000001000000000000000
            sleep(0.5)
        mem32[GPIO_OUT_REG] = 0b00000000000011000000000000000100
        sleep(1)  # Tiempo fijo