from firebase import firebase
firebase = firebase.FirebaseApplication('https://marmitech-1b071.firebaseio.com/')
result = firebase.get('user', None)
print (result)
{'1': 'John Doe', '2': 'Jane Doe'}