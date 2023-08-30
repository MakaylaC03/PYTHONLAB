import RPi.GPIO as GPIO
import time

SERVO_PIN = 18
TRIGGER_PIN = 19
ECHO_PIN = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(SERVO_PIN, GPIO.OUT)
pwm = GPIO.PWM(SERVO_PIN,50)
pwm.start(6.5)
time.sleep(1)
pwm.ChangeDutyCycle(0)


try:
    def distance():
        GPIO.output(TRIGGER_PIN, True)
        time.sleep(0.1)
        GPIO.output(TRIGGER_PIN, False)

        while GPIO.input(ECHO_PIN)==False:
            t_tx = time.time()
        while GPIO.input(ECHO_PIN)==True:
            t_tr = time.time()

        distance = ((t_tr - t_tx)*34300)/2
        print("object distance is: ", distance,"cm")
        print("trip time is: ",(t_tr-t_tx)*1000,"ms")
        time.sleep(1)
        return distance
finally:
    GPIO.cleanup

try:
    while True:
        duty_cycle = 1
        for x in range(4):
            duty_cycle+=3
            print('Sensor is at duty cycle: ',duty_cycle)

            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(1)
            pwm.ChangeDutyCycle(0)
            time.sleep(0.5)

            distance()
            time.sleep(0.1)
        for x in range(4):
            duty_cycle-=3
            print('Sensor is at duty cycle: ',duty_cycle)

            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(1)
            pwm.ChangeDutyCycle(0)
            time.sleep(0.5)

            distance()
            time.sleep(0.1)

finally:
    GPIO.cleanup
