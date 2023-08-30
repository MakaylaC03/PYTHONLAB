import RPi.GPIO as GPIO
import time
from time import sleep

SERVO_PIN = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(SERVO_PIN, GPIO.OUT)
pwm = GPIO.PWM(SERVO_PIN,50)
pwm.start(6.5)
sleep(1)
pwm.ChangeDutyCycle(0)

try:
    while True:
        duty_cycle = 1
        for x in range(4):
            duty_cycle+=3
            print(duty_cycle)

            pwm.ChangeDutyCycle(duty_cycle)
            sleep(1)
            pwm.ChangeDutyCycle(0)
            sleep(0.5)
        for x in range(4):
            duty_cycle-=3
            print(duty_cycle)

            pwm.ChangeDutyCycle(duty_cycle)
            sleep(1)
            pwm.ChangeDutyCycle(0)
            sleep(0.5)

finally:
    GPIO.cleanup
