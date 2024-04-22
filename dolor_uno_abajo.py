import RPi.GPIO as GPIO
from pythonosc import dispatcher, osc_server
import neopixel
import Adafruit_GPIO.SPI as SPI
import board
import busio
import digitalio
import time
import adafruit_tlc5947

# Define el pin GPIO que deseas utilizar para PWM (por ejemplo, GPIO 13)
pin_lillyPad1 = 27
pin_lillyPad2 = 26
pin_lillyPad3 = 13
pin_lillyPad4 = 12

GPIO.setup(pin_lillyPad1, GPIO.OUT)
GPIO.setup(pin_lillyPad2, GPIO.OUT)
GPIO.setup(pin_lillyPad3, GPIO.OUT)
GPIO.setup(pin_lillyPad4, GPIO.OUT)
pwm_lillyPad1 = GPIO.PWM(pin_lillyPad1, 100)
pwm_lillyPad2 = GPIO.PWM(pin_lillyPad2, 100)
pwm_lillyPad3 = GPIO.PWM(pin_lillyPad3, 100)
pwm_lillyPad4 = GPIO.PWM(pin_lillyPad4, 100)
pwm_lillyPad1.start(0)
pwm_lillyPad2.start(0)
pwm_lillyPad3.start(0)
pwm_lillyPad4.start(0)

SCK = board.SCK
MOSI = board.MOSI
LATCH = digitalio.DigitalInOut(board.D5)

number_of_boards = 1
number_of_channels = number_of_boards * 6

spi = busio.SPI(clock=SCK, MOSI=MOSI)

tlc5947 = adafruit_tlc5947.TLC5947(spi, LATCH)

pins = [0]*(number_of_channels)

for channel in range(len(pins)):
    pins[channel] = tlc5947.create_pwm_out(channel)
    
#neopixel

num_neopixels = [4,4,3,3]
brillo = 1.0
constelacion_mitzi = neopixel.NeoPixel(board.D12, num_neopixels[0], brightness=brillo, auto_write=False)
constelacion_lynnette = neopixel.NeoPixel(board.D21, num_neopixels[1], brightness=brillo, auto_write=False)

#constelacion_mitzi = neopixel.NeoPixel(board.D10, num_pixels, brightness=brillo, auto_write=False)
#limpia neopixels
#constelacion_lynnette.deinit()
#constelacion_lynnette.deinit()

#valor = 0


def custom_map(value, start1, stop1, start2, stop2):
    """
    Mapea el valor desde el rango (start1, stop1) al rango (start2, stop2).
    """
    return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))



# Define funciones para manejar los mensajes OSC y controlar los LEDs
def manejar_led(address, *args):
    #print(f"Recibido mensaje desde {address}: {args}")
    #Comienza Mitzi
    if address == "/neopixel1Mitzi":
        #print(args[0])
        mitzi1_r = args[0]
        mitzi1_g = args[1]
        mitzi1_b = args[2]
        mitzi1_i = args[3]
        mitzi1_r_new  = custom_map(mitzi1_i, 0, 255, 0, mitzi1_r)
        mitzi1_g_new  = custom_map(mitzi1_i, 0, 255, 0, mitzi1_g)
        mitzi1_b_new  = custom_map(mitzi1_i, 0, 255, 0, mitzi1_b)
        constelacion_mitzi[0] = (mitzi1_r_new,mitzi1_g_new, mitzi1_b_new)
        constelacion_mitzi.show()
    elif address == "/neopixel2Mitzi":
        mitzi2_r = args[0]
        mitzi2_g = args[1]
        mitzi2_b = args[2]
        mitzi2_i = args[3]
        mitzi2_r_new  = custom_map(mitzi2_i, 0, 255, 0, mitzi2_r)
        mitzi2_g_new  = custom_map(mitzi2_i, 0, 255, 0, mitzi2_g)
        mitzi2_b_new  = custom_map(mitzi2_i, 0, 255, 0, mitzi2_b)
        constelacion_mitzi[1] = (mitzi2_r_new,mitzi2_g_new, mitzi2_b_new)
        constelacion_mitzi.show()
    elif address == "/neopixel3Mitzi":
        mitzi3_r = args[0]
        mitzi3_g = args[1]
        mitzi3_b = args[2]
        mitzi3_i = args[3]
        mitzi3_r_new  = custom_map(mitzi3_i, 0, 255, 0, mitzi3_r)
        mitzi3_g_new  = custom_map(mitzi3_i, 0, 255, 0, mitzi3_g)
        mitzi3_b_new  = custom_map(mitzi3_i, 0, 255, 0, mitzi3_b)
        constelacion_mitzi[2] = (mitzi3_r_new,mitzi3_g_new, mitzi3_b_new)
        constelacion_mitzi.show()
    elif address == "/neopixel4Mitzi":
        mitzi4_r = args[0]
        mitzi4_g = args[1]
        mitzi4_b = args[2]
        mitzi4_i = args[3]
        mitzi4_r_new  = custom_map(mitzi4_i, 0, 255, 0, mitzi4_r)
        mitzi4_g_new  = custom_map(mitzi4_i, 0, 255, 0, mitzi4_g)
        mitzi4_b_new  = custom_map(mitzi4_i, 0, 255, 0, mitzi4_b)
        constelacion_mitzi[3] = (mitzi4_r_new,mitzi4_g_new, mitzi4_b_new)
        constelacion_mitzi.show()
    #Comienza Lynnette
    elif address == "/neopixel1Lynnette":
        lynnette1_r = args[0]
        lynnette1_g = args[1]
        lynnette1_b = args[2]
        lynnette1_i = args[3]
        lynnette1_r_new  = custom_map(lynnette1_i, 0, 255, 0, lynnette1_r)
        lynnette1_g_new  = custom_map(lynnette1_i, 0, 255, 0, lynnette1_g)
        lynnette1_b_new  = custom_map(lynnette1_i, 0, 255, 0, lynnette1_b)
        constelacion_lynnette[0] = (lynnette1_r_new, lynnette1_g_new, lynnette1_b_new)
        constelacion_lynnette.show()
    elif address == "/neopixel2Lynnette":
        lynnette2_r = args[0]
        lynnette2_g = args[1]
        lynnette2_b = args[2]
        lynnette2_i = args[3]
        lynnette2_r_new  = custom_map(lynnette2_i, 0, 255, 0, lynnette2_r)
        lynnette2_g_new  = custom_map(lynnette2_i, 0, 255, 0, lynnette2_g)
        lynnette2_b_new  = custom_map(lynnette2_i, 0, 255, 0, lynnette2_b)
        constelacion_lynnette[1] = (lynnette2_r_new, lynnette2_g_new, lynnette2_b_new)
        constelacion_lynnette.show()
    elif address == "/neopixel3Lynnette":
        lynnette3_r = args[0]
        lynnette3_g = args[1]
        lynnette3_b = args[2]
        lynnette3_i = args[3]
        lynnette3_r_new  = custom_map(lynnette3_i, 0, 255, 0, lynnette3_r)
        lynnette3_g_new  = custom_map(lynnette3_i, 0, 255, 0, lynnette3_g)
        lynnette3_b_new  = custom_map(lynnette3_i, 0, 255, 0, lynnette3_b)
        constelacion_lynnette[2] = (lynnette3_r_new, lynnette3_g_new, lynnette3_b_new)
        constelacion_lynnette.show()
    elif address == "/neopixel4Lynnette":
        lynnette4_r = args[0]
        lynnette4_g = args[1]
        lynnette4_b = args[2]
        lynnette4_i = args[3]
        lynnette4_r_new  = custom_map(lynnette4_i, 0, 255, 0, lynnette4_r)
        lynnette4_g_new  = custom_map(lynnette4_i, 0, 255, 0, lynnette4_g)
        lynnette4_b_new  = custom_map(lynnette4_i, 0, 255, 0, lynnette4_b)
        constelacion_lynnette[3] = (lynnette4_r_new, lynnette4_g_new, lynnette4_b_new)
        constelacion_lynnette.show()
    elif address == "/led1Mitzi":
        led1 = args[0]
        led1 = custom_map(led1,0,255,0, 100)
        pwm_lillyPad1.ChangeDutyCycle(led1)
        
    elif address == "/led2Mitzi":
        led2 = args[0]
        led2 = custom_map(led2,0,255,0, 100)
        pwm_lillyPad2.ChangeDutyCycle(led2)
        
    elif address == "/led1Lynnette":
        led3 = args[0]
        led3 = custom_map(led3,0,255,0, 100)
        pwm_lillyPad3.ChangeDutyCycle(led3)
    elif address == "/led2Lynnette":
        led4 = args[0]
        led4 = custom_map(led4,0,255,0, 100)
        pwm_lillyPad4.ChangeDutyCycle(led4)
    #time.sleep(0.001)
    
# Crea un despachador de mensajes OSC
dispatcher = dispatcher.Dispatcher()

# Mapea las direcciones OSC a la función de manejo
direcciones_osc = ["/neopixel1Lynnette","/neopixel2Lynnette","/neopixel3Lynnette","/neopixel4Lynnette","/neopixel1Mitzi","/neopixel2Mitzi","/neopixel3Mitzi","/neopixel4Mitzi","/led1Mitzi","/led2Mitzi","/led1Lynnette","/led2Lynnette","/led3Lynnette"]
for direccion in direcciones_osc:
    dispatcher.map(direccion, manejar_led)

# Configura y corre el servidor OSC en el hilo principal
ip_escucha = "0.0.0.0"  # Escucha en todas las interfaces de red
puerto_escucha = 8000   # Puerto en el que escucha el servidor

servidor = osc_server.BlockingOSCUDPServer((ip_escucha, puerto_escucha), dispatcher)
print(f"Escuchando en {ip_escucha}:{puerto_escucha}")

# Inicia el servidor
servidor.serve_forever()

# Detiene el PWM y limpia los pines GPIO al finalizar
pwm_lillyPad1.stop()
GPIO.cleanup()
