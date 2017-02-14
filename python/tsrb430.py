# class to hold read and write
#!/usr/bin/env python

import serial
import logging
import time, datetime
from firebase import firebase
from firebase_token_generator import create_token
from apscheduler.schedulers.blocking import BlockingScheduler

class AIHome:

	def __init__(self, onTime, offTime):
	
		self.onTime=onTime
		self.offTime=offTime
		self.updateInterval = 6
		self.webPush = False
		self.relayStatesA = []
		self.relayStatesD = {}
		logging.basicConfig()
		#Call fetchUpdate every 6 hours
		
		print('initting AIHome...scheduling job')
		sched = BlockingScheduler()
		@sched.scheduled_job('interval', hours=1)
		def timed_job():
			print('This job runs every 6 hrs. timed_job gets called or something else')
			#call fetchUpdate()
			self.fetchUpdate();
			
		#RUNS AT DAY&TIME SPECIIFIED###########################
		#@sched.scheduled_job('cron', day_of_week='mon-fri', hour=12)
		#def scheduled_job():
		#	print('This job is run every weekday at 12pm.')
		#######################################################
		
		sched.configure()
		#options_from_ini_file
		sched.start()
		
	# This method gets data and stores it to 
	def fetchUpdate(self):
		AIHome.authentication = firebase.FirebaseAuthentication('zxQ4f3gX9DXBBfHbrCupNqlZgVbDay9klY6zXxkz', 'info@santiapps.com', extra={'id': 123})
		AIHome.firebase = firebase.FirebaseApplication('https://stapp-48d1b.firebaseio.com/', AIHome.authentication)
		print AIHome.authentication.extra

		AIHome.user = AIHome.authentication.get_user()
		print AIHome.user.firebase_auth_token

		#Data format returned = {u'Relay1ON': 1800, u'Relay1OFF': u'0600'} 
		AIHome.results = AIHome.firebase.get('/Relays', None)#, {'print': 'pretty'})
		print AIHome.results
		
		#Commented out for debugging purposes
		print AIHome.results['Relay1ON']
		print AIHome.results['Relay1OFF']
		
		#Call time comparator method
		self.relayToggle()
		

		
	def relayToggle(self):
	
		#parse received data
		times1OFF = AIHome.results['Relay1OFF']
		times1ON = AIHome.results['Relay1ON']
		print times1OFF
		print times1ON
		hours1OFF,minutes1OFF = times1OFF.split(":")
		hours1ON,minutes1ON = times1ON.split(":")
		print hours1OFF
		print minutes1OFF
		print hours1ON
		print minutes1ON
		print(datetime.datetime.now())
		ref_time1OFF = datetime.datetime.combine(datetime.datetime.now(), datetime.time(int(hours1OFF), int(minutes1OFF)))
		ref_time1ON = datetime.datetime.combine(datetime.datetime.now(), datetime.time(int(hours1ON), int(minutes1ON)))
		if ref_time1OFF < datetime.datetime.now() and datetime.datetime.now() < ref_time1ON:
			print("ref_time>relay should be OFF")
			self.write(1,0)
		else:
			print("now>relay should be ON")
			self.write(1,1)			
# 		while True:
# 		   now_time = datetime.time()
# 		   now_time_string = time.strftime("%H:%M:%S")
# 		   print("now_time")
# 		   print now_time_string
# 
# 		   #Get results.Relay1ON & OFF to compare...
# 		   timeon_time = results.Relay1ON
# 		   #timeon_time = datetime.time(18, 00, 00, 000000)
# 		   print("timeon_time")
# 		   print timeon_time
# 	   
# 		   if now_time<timeon_time: print("toggle off write(self,1,0)")
# 		   else: print("toggle relay on")
	
	
	#Toggle specified relay
	def write(self, relay, state):
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
		print relay
		print state
		#self.read()
		#ser.write("AT+CONNL")
		
		#switch case
		while True:
			# Relay1ON 1
			if relay == 1 & state == 0:
				ser.write("o")
				print ('Relay toggled off')
				break

			# case 2
			if relay == 1 & state == 1:
				ser.write("e")
				print ('Relay toggled on')
				break

			# else case 3
			print ('something else')
			ser.write("o")
			x=ser.readline()
			print "After w, got '" + x + "'"
			break
		
		
		print "Did write, now read"
		x = ser.readline()
		print "got '" + x + "'"
		print "Writing & Reading got '" + x + "'"
		#self.read()
		ser.close()
	
	
	def convert_hex_to_int(self,hexChars):
		#convert string of hex chars to a list of ints
		try:
			ints = [ord(char) for char in hexChars]
			return ints
		except TypeError:
			pass
		return []
	
	def convert_hex_to_bin_str(self,hexChars):
		#convert hex char into byte string
		response = convert_hex_to_int(hexChars)[0]
		# convert int to binary string
		responseBinary = bin(response)
		# first 2 chars of binary string are '0b' so ignore these
		return responseBinary[2:]	
	
	# To be used later when fetching relay states from app or web
	def read(self):
		ser = serial.Serial(
			port='/dev/serial0',
			baudrate=9600,
			parity=serial.PARITY_NONE,
			stopbits=serial.STOPBITS_ONE,
			bytesize=serial.EIGHTBITS,
			timeout=1
		)

		print "Read:Serial is open: " + str(ser.isOpen())
		print "Read:Now Reading"
		ser.write("[")
		print "Did read"
		x = ser.readline()
		print "Read:Reading got '" + x + "'"
		responseBits = convert_hex_to_bin_str (x)
		responseBits = responseBits.zfill(4)
		responseBits = list(responseBits)
		responseBits.reverse()
		relayStates = {}
		relay = 1
		for bit in responseBits:
			relayStates[relay] = int(bit)
			relay += 1
		self.relayStatesD = relayStates
		#report states to someone?
		print relayStatesD
		#ser.close()



x = AIHome(1,2)

# For future user prompt admin panel
# usercommand=''
# print "Hello! ";
# 
# while name !='quit':
# 	usercommand = raw_input('enter a command:')
# 	if (usercommand == "[") {
# 		getting data to print
# 		call read function from class below
# 		} else {
# 		call write function from class below
# 		self.write(usercommand)
# 		wait for response
# 		call read function from class below
# 		}
