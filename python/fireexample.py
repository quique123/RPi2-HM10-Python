import datetime

from firebase.firebase import FirebaseApplication, FirebaseAuthentication


if __name__ == '__main__':
    SECRET = 'sod123'
    DSN = 'https://stapp-48d1b.firebaseio.com'
    EMAIL = 'info@santiapps.com'
    authentication = FirebaseAuthentication(SECRET,EMAIL, True, True)
    firebase = FirebaseApplication(DSN, authentication)

    firebase.get('/users', None,
                 params={'print': 'pretty'})
#                 headers={'X_FANCY_HEADER': 'very fancy'})

    data = {'name': 'Ozgur Vatansever', 'age': 26,
            'created_at': datetime.datetime.now()}

    snapshot = firebase.post('/users', data)
    print(snapshot['name'])

    def callback_get(response):
        with open('/dev/null', 'w') as f:
            f.write(response)
    firebase.get_async('/users', snapshot['name'], callback=callback_get)

