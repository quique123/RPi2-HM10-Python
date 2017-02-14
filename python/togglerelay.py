#!/usr/bin/env python

import serial

ser = serial.Serial(
	port='/dev/serial0',
	baudrate=9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1
)

print "Serial is open: " + str(ser.isOpen())

print "Now Writing"
ser.write("e")
#ser.write("AT+CONNL")
print "Did write, now read"
x = ser.readline()
print "got '" + x + "'"

ser.close()

