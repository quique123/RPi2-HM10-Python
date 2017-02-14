# Might need time library to check data often
# Might need requests if we dont use urllib2
# Definitely need json
# Might need serial if we combine both this and ble control script tsrb430.py or 
import time
import requests
import json
import urllib2

# 1. Initialization code
var config = {
	apiKey: "AIzaSyA30Y3Gw-pqKAu1rnUxdrGyRHmRyfWGUm0",
	authDomain: "stapp-48d1b.firebaseapp.com",
	databaseURL: "https://stapp-48d1b.firebaseio.com",
	storageBucket: "stapp-48d1b.appspot.com",
	messagingSenderId: "699536324681"}

firebase.initializeApp(config)

# 2. configure db 
db = firebase.FirebaseApplication('https://myfirebase.firebaseio.com/')

# 3. set api url
api = "https://stapp-48d1b.firebaseio.com/timeoff.json"
get = urllib2.urlopen(api).read()

# 4. Debug result
print get






# X. write data
#db.post('/testval/',1)

#GIthub Project examples for getting data from firebase
# from firebase import firebase
# 
# FIREBASE_URL = "https://dazzling-fire-5952.firebaseio.com/"
# 
# # Main
# if __name__ == '__main__':
#     fb = firebase.FirebaseApplication(FIREBASE_URL, None) # Create a reference to the Firebase Application
# 
#     result = fb.get('/PythonDemo', "Node1") # Get  data from firebase
# 
#     print("FB Data = %s" % result)