#!/usr/bin/env python

import serial
import tosrx

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
#ser.write("AT")
ser.write("[")
print "Did write, now read"
x = ser.readline()
print "got '" + x + "'"

ser.close()

#conversion helpers
def convert_hex_to_int(hexChars):
    '''convert string of hex chars to a list of ints'''

    try:
        ints = [ord(char) for char in hexChars]
        return ints
    except TypeError:
        pass
    return []

def convert_hex_to_bin_str(hexChars):
    '''convert hex char into byte string'''

    response = convert_hex_to_int(hexChars)[0]
    # convert int to binary string
    responseBinary = bin(response)
    # first 2 chars of binary string are '0b' so ignore these
    return responseBinary[2:]
