#!/usr/bin/env python

import serial

def convert_hex_to_int(hexChars):
    #convert string of hex chars to a list of ints
    try:
        ints = [ord(char) for char in hexChars]
        return ints
    except TypeError:
        pass
    return []
def convert_hex_to_bin_str(hexChars):
    #convert hex char into byte string
    response = convert_hex_to_int(hexChars)[0]
    # convert int to binary string
    responseBinary = bin(response)
    # first 2 chars of binary string are '0b' so ignore these
    return responseBinary[2:]

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
#ser.write("[")
ser.write("AT+CONNL")
print "Did write, now read"
x = ser.readline()
print "got '" + x + "'"

responseBits = convert_hex_to_bin_str (x)
# binary conversion drops values until a 1 is encountered
# assume missing values are 0 and pad to give a value for all relays
responseBits = responseBits.zfill(4)
# reverse chars so that relay 1 is first
responseBits = list(responseBits)
responseBits.reverse()
# create dictionary of relay states
relayStates = {}
relay = 1
for bit in responseBits:
    relayStates[relay] = int(bit)
    relay += 1
print relayStates

ser.close()

