from firebase import firebase
firebase = firebase.FirebaseApplication('https://marmitech-1b071.firebaseio.com/')
#result = firebase.post('marmitech-1b071',{'dias': {'segunda':' macarrao', 'terca':'pf', 'quarta':'peixes', 'quinta':'lasanha','sexta':'feijoada' }})
#result = firebase.post('marmitech-1b071', {'pedidos':'pedidos_usuario'})
#result = firebase.post('marmitech-1b071', {'usuario': 'tipos'})
result = firebase.post('marmitech-1b071',{'login':'letras','senha':'numeros_letrasminusculas'})
print (result)
