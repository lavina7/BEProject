import RPi.GPIO as GPIO
import time
import MySQLdb as mdb
import threading
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
thread_lock = threading.Lock()
con=mdb.connect('localhost','root','root','parking');

def light():
    s=""
    thread_lock.acquire()
    with con:
        cursor=con.cursor()
        cursor.execute("SELECT status from slots")
        row = cursor.fetchall()
        for i in row:
            s+=str(i[0])
        cursor.close()
        if s=="0000":
            GPIO.output(14,GPIO.LOW)
            GPIO.output(15,GPIO.LOW)        
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.LOW)

        elif s=="0001":
            GPIO.output(14,GPIO.LOW)
            GPIO.output(15,GPIO.LOW)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.HIGH)
        elif s=="0010":
            GPIO.output(14,GPIO.LOW)
            GPIO.output(15,GPIO.LOW)        
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(23,GPIO.LOW)
        elif s=="0011":
            GPIO.output(14,GPIO.LOW)
            GPIO.output(15,GPIO.LOW)        
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(23,GPIO.HIGH)
        elif s=="0100":
            GPIO.output(14,GPIO.LOW)
            GPIO.output(15,GPIO.HIGH)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.LOW)
        elif s=="0101":
            GPIO.output(14,GPIO.LOW)
            GPIO.output(15,GPIO.HIGH)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.HIGH)
        elif s=="0110":
            GPIO.output(14,GPIO.LOW)
            GPIO.output(15,GPIO.HIGH)
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(23,GPIO.LOW)
        elif s=="0111":
            GPIO.output(14,GPIO.LOW)
            GPIO.output(15,GPIO.HIGH)
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(23,GPIO.HIGH)
        elif s=="1000":
            GPIO.output(14,GPIO.HIGH)
            GPIO.output(15,GPIO.LOW)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.LOW)
        elif s=="1001":
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(14,GPIO.LOW)
            GPIO.output(15,GPIO.LOW)
            GPIO.output(23,GPIO.HIGH)
        elif s=="1010":
            GPIO.output(14,GPIO.HIGH)
            GPIO.output(15,GPIO.LOW)
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(23,GPIO.LOW)
        elif s=="1011":
            GPIO.output(14,GPIO.HIGH)
            GPIO.output(15,GPIO.LOW)
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(23,GPIO.HIGH)
        elif s=="1100":
            GPIO.output(14,GPIO.HIGH)
            GPIO.output(15,GPIO.HIGH)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.LOW)
        elif s=="1101":
            GPIO.output(14,GPIO.HIGH)
            GPIO.output(15,GPIO.HIGH)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.HIGH)
        elif s=="1110":
            GPIO.output(14,GPIO.HIGH)
            GPIO.output(15,GPIO.HIGH)
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(23,GPIO.LOW)
        elif s=="1111":
            GPIO.output(14,GPIO.HIGH)
            GPIO.output(15,GPIO.HIGH)
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(23,GPIO.HIGH)
        time.sleep(2)
        thread_lock.release()

while True :
    light();
    time.sleep(1)
    




