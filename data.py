#!/usr/bin/env python
import time
import serial
import threading
import MySQLdb as mdb
import schedule

con0=mdb.connect('localhost','root','root','parking');
con1=mdb.connect('localhost','root','root','parking');
ser0 = serial.Serial('/dev/ttyUSB0', 9600)
ser1 = serial.Serial('/dev/ttyUSB1', 9600)
time.sleep(2)

thread_lock = threading.Lock()


def sensor0():
    time.sleep(2)
    writer = threading.Thread(target=serialRW0, args=['sensor#'])
    writer.start()
    
def sensor1():
    time.sleep(2)
    writer = threading.Thread(target=serialRW1, args=['sensor#'])
    writer.start()
    
def serialRW0(com):
    
    if(ser0.inWaiting > 0):
        output0=ser0.readline()
        output_string0 = output0.strip()
        print output_string0
        if output_string0 == "a0b0" :
            with con0:
                cursor=con0.cursor()
                query="""UPDATE slots SET status = %s WHERE slotid = %s"""
                data1 =(0,1)
                query2="""UPDATE slots SET status = %s WHERE slotid = %s"""
                data2= (0,2)
                cursor.execute(query,data1)
                cursor.execute(query2,data2)
                con0.commit()
                cursor.close()
        elif output_string0 =="a1b1" :
            with con0:
                cursor=con0.cursor()
                query="""UPDATE slots SET status = %s WHERE slotid = %s"""
                data1 =(1,1)
                query2="""UPDATE slots SET status = %s WHERE slotid = %s"""
                data2= (1,2)
                cursor.execute(query,data1)
                cursor.execute(query2,data2)
                con0.commit()
                cursor.close()
        elif output_string0 =="a1b0" :
            with con0:
                cursor=con0.cursor()
                query="""UPDATE slots SET status = %s WHERE slotid = %s"""
                data1 =(1,1)
                query2="""UPDATE slots SET status = %s WHERE slotid = %s"""
                data2= (0,2)
                cursor.execute(query,data1)
                cursor.execute(query2,data2)
                con0.commit()
                cursor.close()
        elif output_string0 =="a0b1" :
            with con0:
                cursor=con0.cursor()
                query="""UPDATE slots SET status = %s WHERE slotid = %s"""
                data1 =(0,1)
                query2="""UPDATE slots SET status = %s WHERE slotid = %s"""
                data2= (1,2)
                cursor.execute(query,data1)
                cursor.execute(query2,data2)
                con0.commit()
                cursor.close()
    time.sleep(1)
        
def serialRW1(com):
    
    if(ser1.inWaiting > 0):
        output1=ser1.readline()
        output_string1 = output1.strip()
        print output_string1
        if output_string1 == "c0d0" :
            with con1:
                cursor=con1.cursor()
                query="""UPDATE slots SET status = %s WHERE slotid = %s"""
                data1 =(0,3)
                query2="""UPDATE slots SET status = %s WHERE slotid = %s"""
                data2= (0,4)
                cursor.execute(query,data1)
                cursor.execute(query2,data2)
                con1.commit()
                cursor.close()
        elif output_string1=="c1d1" :
            with con1:
                cursor=con1.cursor()
                query="""UPDATE slots SET status = %s WHERE slotid = %s"""
                data1 =(1,3)
                query2="""UPDATE slots SET status = %s WHERE slotid = %s"""
                data2= (1,4)
                cursor.execute(query,data1)
                cursor.execute(query2,data2)
                con1.commit()
                cursor.close()
        elif output_string1 =="c1d0" :
            with con1:
                cursor=con1.cursor()
                query="""UPDATE slots SET status = %s WHERE slotid = %s"""
                data1 =(1,3)
                query2="""UPDATE slots SET status = %s WHERE slotid = %s"""
                data2= (0,4)
                cursor.execute(query,data1)
                cursor.execute(query2,data2)
                con1.commit()
                cursor.close()
        elif output_string1 =="c0d1" :
            with con1:
                cursor=con1.cursor()
                query="""UPDATE slots SET status = %s WHERE slotid = %s"""
                data1 =(0,3)
                query2="""UPDATE slots SET status = %s WHERE slotid = %s"""
                data2= (1,4)
                cursor.execute(query,data1)
                cursor.execute(query2,data2)
                con1.commit()
                cursor.close()
    time.sleep(1)
    

while True:
    thread_lock.acquire()
    sensor0()
    sensor1()
    time.sleep(3)
    thread_lock.release()
