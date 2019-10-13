import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    input_state = GPIO.input(23)
    input_stat2 = GPIO.input(24)

    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
    if input_state2 == False:
        print('Button Pressed')
        time.sleep(0.2)
