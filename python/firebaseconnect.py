from firebase import firebase
from firebase.firebase import FirebaseApplication, FirebaseAuthentication

authentication = firebase.FirebaseAuthentication('sod123', 'info@santiapps.com', extra={'id': 123})
firebase = firebase.FirebaseApplication('https://stapp-48d1b.firebaseio.com', authentication)
firebase.authentication = authentication
print authentication.extra

user = authentication.get_user()
print user.firebase_auth_token

result = firebase.get('/messages', None)
#result = firebase.get('/grocery-items', None, {'print': 'pretty'})
#result = firebase.get('/messages', None, {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'})
print result
