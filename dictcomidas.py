from firebase import firebase
from flask import Flask, render_template, request, url_for, redirect, send_from_directory
import os


Marmitech = firebase.FirebaseApplication('https://marmitech-1b071.firebaseio.com/')
usuario=[]
vendedor=[]
nomedapessoa=[]
email=[]
comida=[]
# pedido=[]
pedidototal=[]


class Vendedor ():
	def __init__ (self,nomedapessoa,email,senha):
		self.nomedapessoa= nomedapessoa
		self.email=email
		self.senha= senha
		self.comida=[]
		self.dictvendedores={}

	def SalvarVendedor(self):
		# self.dictvendedor[self.nomedapessoa]=[self.email,self.senha,self.comida]
		# listaVendedores = []
		# listaVendedores.append(self.comida)
		# listaVendedores.append(self.senha)	
		# listaVendedores.append(self.email)
		# return self.dictvendedores
		self.dictvendedor["nomedovendedor"]=self.nomedovendedor
		self.dictvendedor["email"]=self.email
		self.dictvendedor["senha"]=self.senha
		self.dictvendedor["pedidototal"]=self.pedidototal
		telavendedor=Marmitech.post('marmitech-1b071',vendedor[0].SalvarVendedor())


class Cliente():
	def __init__(self,nomedapessoa,email,senha):
		self.nomedapessoa=nomedapessoa
		self.email=email
		self.senha=senha
		self.pedidototal=pedidototal
		self.dictcliente={}	
	
	def SalvarCliente(self):
		# self.dictcliente[self.pedidototal]=self.pedidototal,self.senha,self.nomedapessoa
		# listaClientes = []
		# listaVendedores.append(self.pedidototal)
		# listaVendedores.append(self.senha)	
		# listaVendedores.append(self.email)
		# return self.dictcliente
		self.dictcliente["nomedapessoa"]=self.nomedapessoa
		self.dictcliente["email"]=self.email
		self.dictcliente["senha"]=self.senha
		self.dictcliente["pedidototal"]=self.pedidototal
		telacliente=Marmitech.post('marmitech-1b071',usuario[0].SalvarCliente())



app = Flask(__name__, static_url_path='')

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
    
@app.route('/uploads/<filename>')

def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)



 @app.route('/', methods=['POST','GET'])



#telacliente= firebase.put('marmitech-1b071',{dictcliente})
#telavendedor= firebase.post('marmitech-1b071',{dictvendedores})
def validar(): 
	if request.method= 'POST':
		nomedapessoa=request.form['nomedapessoa']
		senha=request.form['senha']
		ler=Marmitech.get('marmitech-1b071','-Kl_awU2thszeeh9okfl',None)

		if nomedapessoa in ler:
			listasenha=[]
			ver=Marmitech.get('marmitech-1b071','-Kl_awU2thszeeh9okfl',None)
			listasenha.append(ver)
			if senha in listasenha:
				return render_template('PaginaHome.html', nomedapessoa=nomedapessoa)
			else:
			x= 'Senha Incorreta'
			return render_template('PaginaCadastroUser.html', nomedapessoa=nomedapessoa, dic=Marmitech.get('marmitech-1b071','-Kl_awU2thszeeh9okfl',None))	
		else:
			x= 'Usuario Inválivo'
			return render_template('PaginaCadastroUser.html', nomedapessoa=nomedapessoa, dic='PaginaCadastroUser.html')	
	return render_template('PaginaHome.html')
	

@app.route('/login', methods=['POST','GET'])	

def perfil():
	usuario=request.args['usuario']
	try:
		






# #listaVendedores = []
# listausuario=[]
# listasenha=[]
# #vend = Vendedor(xyz,"antonio@hotmail.com","1234")
# v=Vendedor(usu,sen,)
# usu=Vendedor("helio")
# # listaVendedores.append(vend)
# listasenha.append(sen)
# listausuario.append(usu)


# # vend = Vendedor("joao","joao@hotmail.com","12345")
# # listaVendedores.append(vend)
# telavendedor=Marmitech.post('marmitech-1b071',listausuario[0].SalvarVendedor())

# telavendedor = Marmitech.post('marmitech-1b071',listasenha[0].SalvarVendedor())