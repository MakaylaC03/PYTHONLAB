import RPi.GPIO as GPIO
import time
import myLCD

#LCD Pins
RGSLCT = 4
ENBL = 17
BACKLIGHT = 26
D4=5
D5=6
D6=13
D7=19

#Servo & Sensor Pins
SERVO_PIN = 18
TRIGGER_PIN = 16
ECHO_PIN = 24

LN1 = 1
LN2 = 2

GPIO.setmode(GPIO.BCM)

GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(SERVO_PIN, GPIO.OUT)
pwm = GPIO.PWM(SERVO_PIN,50)
pwm.start(0)
time.sleep(1)
pwm.ChangeDutyCycle(0)
myLCD.start(GPIO,2,6)

myLCD.LCD(GPIO,RGSLCT,ENBL,D4,D5,D6,D7,BACKLIGHT)

myLCD.lcd_init(GPIO)
myLCD.backlight(GPIO, True)

upArrow=[0x04,0x0E,0x15,0x04,0x04,0x04,0x04,0x04]
leftCornerArrow=[0x1C,0x18,0x14,0x02,0x01,0x00,0x00,0x00]
leftArrow=[0x00,0x00,0x04,0x08,0x1F,0x08,0x04,0x00]
rightCornerArrow=[0x07,0x03,0x05,0x08,0x10,0x00,0x00,0x00]
rightArrow=[0x00,0x00,0x04,0x02,0x1F,0x02,0x02,0x00]

myLCD.lcd_custom(GPIO,0,upArrow)
myLCD.lcd_custom(GPIO,2,leftCornerArrow)
myLCD.lcd_custom(GPIO,3,leftArrow)
myLCD.lcd_custom(GPIO,4,rightCornerArrow)
myLCD.lcd_custom(GPIO,5,rightArrow)

near = 0

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
        print("Object distance is: ", distance,"mm")
        print("trip time is: ",(t_tr-t_tx)*1000,"ms")
        myLCD.lcd_string(GPIO,chr(x) + str(round(distance,1))+"cm", LN1)
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
            return_distance=distance()
            
            if(near==0):
                near=return_distance
            if( return_distance <= near):
                print(return_distance)
                near=return_distance
                a=x
                myLCD.lcd_string(GPIO,"Near:"+chr(x)+str(round(near,1))+"cm",LN2)
            else:
                print(near)
                myLCD.lcd_string(GPIO,"Near:"+chr(a)+str(round(near,1))+'cm',LN2)

            time.sleep(0.1)
            
        for x in range(4):
            duty_cycle-=3
            print('Sensor is at duty cycle: ',duty_cycle)
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(1)
            pwm.ChangeDutyCycle(0)
            time.sleep(0.5)

            return_distance=distance()
            
            if(return_distance <= near):
                print(return_distance)
                near=return_distance
                a=x
                myLCD.lcd_string(GPIO,"Near"+chr(x)+str(round(near,1))+"cm",LN2)
            else:
                print(near)
                myLCD.lcd_string(GPIO,"Near:"+chr(a)+str(round(near,1))+"cm",LN2)
                
            time.sleep(0.1)

finally:
    GPIO.cleanup
