from firebase import firebase
Marmitech = firebase.FirebaseApplication('https://marmitech-1b071.firebaseio.com/')
listaVendedores = []
email=[]
comida=[]
pedido=[]
pedidototal=[]


x
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
class login():
	def__init__ (self,nomedapessoa,email,senha):





#telacliente= firebase.put('marmitech-1b071',{dictcliente})
#telavendedor= firebase.post('marmitech-1b071',{dictvendedores})
def validar(listausuario,listasenha):
	if request.method= 'POST':
		nomedapessoa=request.form['nomedapessoa']
		senha=request.form['senha'
		ler=Marmitech.get('marmitech-1b071','-Kl_awU2thszeeh9okfl',None)

#listaVendedores = []
listausuario=[]
listasenha=[]
#vend = Vendedor(xyz,"antonio@hotmail.com","1234")
v=Vendedor(usu,sen,)
usu=Vendedor("helio")
# listaVendedores.append(vend)
listasenha.append(sen)
listausuario.append(usu)


# vend = Vendedor("joao","joao@hotmail.com","12345")
# listaVendedores.append(vend)
telavendedor=Marmitech.post('marmitech-1b071',listausuario[0].SalvarVendedor())

telavendedor = Marmitech.post('marmitech-1b071',listasenha[0].SalvarVendedor())
