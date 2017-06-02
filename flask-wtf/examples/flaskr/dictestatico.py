#dicionario estatico que servira apenas para login
from firebase import firebase

email=[]
comida=[]
pedido=[]
pedidototal=[]


class Vendedor ():
	def __init__ (self,nomedapessoa,email,senha):
		self.nomedapessoa= nomedapessoa
		self.email=email
		self.senha= senha
		self.comida=[]
		self.dictvendedores={}

	def SalvarVendedor(self):
		self.dictvendedores[self.nomedapessoa]=[self.email,self.senha,self.comida]
		listaVendedores = []
		listaVendedores.append(self.comida)
		listaVendedores.append(self.senha)	
		listaVendedores.append(self.email)
		return self.dictvendedores

class Cliente():
	def __init__(self,nomedapessoa,email,senha):
		self.nomedapessoa=nomedapessoa
		self.email=email
		self.senha=senha
		self.pedidototal=pedidototal
		self.pedido=[]
		self.dictcliente={}	
	
	def SalvarCliente(self):
		self.dictcliente[self.pedidototal]=self.pedidototal,self.senha,self.nomedapessoa
		listaClientes = []
		listaVendedores.append(self.pedidototal)
		listaVendedores.append(self.senha)	
		listaVendedores.append(self.email)
		return self.dictcliente

Marmitech = firebase.FirebaseApplication('https://marmitech-1b071.firebaseio.com/')
listaVendedor=[]

vend=Vendedor("Antonio","antonio@hotmail.com","1234")
listaVendedor.append(vend)
vend= Vendedor("ele","eu@ele","1234")
listaVendedor.append(vend)
telavendedor=Marmitech.put('marmitech-1b071',listaVendedor[0].SalvarVendedor())
print (telavendedor)