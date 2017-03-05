import json
import urllib2

# 1. Authentication code
var config = {
	apiKey: "my-key",
	authDomain: "myapp.firebaseapp.com",
	databaseURL: "https://myapp.firebaseio.com",
	storageBucket: "myapp.appspot.com",
	messagingSenderId: "someID"}

firebase.initializeApp(config)

# 2. configure db 
db = firebase.FirebaseApplication('https://myfirebase.firebaseio.com/')

# 3. set api url
api = "https://myapp.firebaseio.com/timeoff.json"
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
