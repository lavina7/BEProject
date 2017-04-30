#Libraries
import RPi.GPIO as GPIO
import time
import serial
import threading

ser = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(2)
ser2 = serial.Serial('/dev/ttyUSB1', 9600)
time.sleep(2)
thread_lock = threading.Lock()
        
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 24
GPIO_ECHO = 25
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setwarnings(False)
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, False)
    time.sleep(2)
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
c=0
while True:
    dist = distance()
    print dist
    if (dist < 5):
        thread_lock.acquire()
        ser.write("light#")
        ser2.write("light#")
        time.sleep(1)
        ser.write("light#")
        ser2.write("light#")
        time.sleep(1)
        ser.write("light#")
        ser2.write("light#")
        time.sleep(1)
        ser.write("light#")
        ser2.write("light#")
        time.sleep(1)
        ser.write("light#")
        ser2.write("light#")
        time.sleep(1)
        ser.write("light#")
        ser2.write("light#")
        time.sleep(1)
        ser.write("light#")
        ser2.write("light#")
        time.sleep(1)
        ser.write("light#")
        ser2.write("light#")
        time.sleep(1)
        ser.write("light#")
        ser2.write("light#")
        time.sleep(1)
        ser.write("light#")
        ser2.write("light#")
        time.sleep(3)
        thread_lock.release()
    else :
        ser.write("lightoff#")
        ser2.write("lightoff#")
  
GPIO.cleanup()
