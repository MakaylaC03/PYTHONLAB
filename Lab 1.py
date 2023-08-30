
#------------------------------------------------------------------------------------------------------------------------------
#
# ECE/Engr. 296, Fall 2022
# Name: Makayla L. Coomer
# Lab 0.1
#
# Basis I/O: Push a button and light an LED
#
#-----------------------------------------------------------------------------------------------------------------------------

# Import libraries
import RPi.GPIO as GPIO
import time

# Assign pin numbers to variables
BUTTON_PIN = 17
LED_PIN = 27

# Set mode to use pin names
GPIO.setmode(GPIO.BCM)

# Setup BUTTON_PIN as input and LED_PIN as output
GPIO.setup(BUTTON_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

# Set LED_PIN to output False (Ground, 0 volts)
GPIO.output(LED_PIN,False)

# Initialize state of LED
on_off = 'off'

#try/finally block (finally: runs when CTRL-C entered)
try:
    # Loop forever
    while True:
        # Check to see if button pressed
        if GPIO.input(BUTTON_PIN) == False:
            # Toggle LED state when pressed
            if on_off == 'off':
                on_off = 'on'
            else:
                on_off = 'off'
        # Wait to debounce button
        time.sleep(0.2)
        # Turn LED on/off
        if on_off == 'on':
            GPIO.output(LED_PIN,True)
            print('on')
        elif on_off == 'off':
            GPIO.output(LED_PIN,False)
            print('off')

# Run when Program interrupt
finally:
    print(' Cleaning up')
    GPIO.cleanup()
