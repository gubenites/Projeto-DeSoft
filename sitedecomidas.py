from firebase import firebase
firebase = firebase.FirebaseApplication('https://marmitech-1b071.firebaseio.com/')
result = firebase.post('marmitech-1b071',{'dias': {'segunda':' macarrao', 'terca':'pf', 'quarta':'peixes', 'quinta':'lasanha','sexta':'feijoada' }})
print (result)
