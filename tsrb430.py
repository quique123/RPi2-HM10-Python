# class to hold read and write
#!/usr/bin/env python

import serial

# user prompt
usercommand=''
print "Hello! ";

while name !='quit':
	usercommand = raw_input('enter a command:')
	if (usercommand == "[") {
		#getting data to print
		#call read function from class below
		} else {
		#call write function from class below
		self.write(usercommand)
		#wait for response
		#call read function from class below
		}
		

class rpiblecomm {

def __init__(self):

def read:
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
	ser.write("[")
	print "Did write, now read"
	x = ser.readline()
	print "got '" + x + "'"
	responseBits = convert_hex_to_bin_str (x)
	responseBits = responseBits.zfill(4)
	responseBits = list(responseBits)
	responseBits.reverse()
	relayStates = {}
	relay = 1
	for bit in responseBits:
		relayStates[relay] = int(bit)
		relay += 1
	print relayStates
	ser.close()

#must pass in usercommand
def write(usercommand):
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
	ser.write(usercommand)
	#ser.write("AT+CONNL")
	print "Did write, now read"
	x = ser.readline()
	print "got '" + x + "'"
	ser.close()

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



}
