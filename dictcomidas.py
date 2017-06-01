from firebase import firebase

Marmitech=firebase.FirebaseApplication('https://marmitech-1b071.firebaseio.com', None)

email=[]
comida1=[]
comida2=[]
comida3=[]
pedido1=[]
pedido2=[]
pedido3=[]
pedidototal=[]


class Vendedores ():
	def __init__ (self,nomedapessoa,email,senha):
		self.nomedapessoa= nomedapessoa
		self.email=email
		self.senha= senha
		self.comida1=[]
		self.comida2=[]
		self.comida3=[]
		self.dictvendedores={}

	def SalvarVendedores(self,nom):
		self.dictvendedores[self.nomedapessoa]=self.nomedapessoa,self.email,self.senha,self.comida1,self.comida2,self.comida3
		email.append(self.email)
		return self.dictvendedores

class Cliente():
	def __init__(self,nomedapessoa,email,senha):
		self.nomedapessoa=nomedapessoa
		self.email=email
		self.senha=senha
		self.pedidototal=pedidototal
		self.pedido1=[]
		self.pedido2=[]
		self.pedido3=[]
		self.dictcliente={}	
	
	def SalvarCliente(self):
		self.dictcliente[self.pedidototal]=self.pedidototal,self.pedidototal.append(self.pedido1),self.pedidototal.append(self.pedido2),self.pedidototal.append(self.pedido3),self.senha,self.nomedapessoa
		email.append(self.email)
		return self.dictcliente



Marmitech=firebase.FirebaseApplication('https://marmitech-1b071.firebaseio.com', None)
# telacliente= firebase.put('marmitech-1b071',{dictcliente})
telavendedor= firebase.post('marmitech-1b071',{dictvendedores})



