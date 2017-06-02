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

#classes para vendedor e cliente, recebendo dados em um nó nominal(por exemplo antonio) que contem todas informações, email, senha e dependendo da interface, pedidos ou tipos de comida
#no firebase ele salva como um nó (nome), que recebe login,senha e email
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
		self.dictvendedor["comida"]=self.comida
		telavendedor=Marmitech.post('marmitech-1b071',vendedor[0].SalvarVendedor())



''' exemplo de subida de dados para de dados nominais 
#listaVendedores = []
# # vend = Vendedor("antonio","antonio@hotmail.com","1234")
# # listaVendedores.append(vend)
# telavendedor=Marmitech.post('marmitech-1b071',listausuario[0].SalvarVendedor())
'''


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


#flask define paginas como pagina principal, pagina about, cadastro de usuarios e vendedores
  
app = Flask(__name__)
  
@app.route('/')
def home():
  return render_template('PaginaHome.html')
  
@app.route('/about')
def about():
  return render_template('About.html')
  
@app.route('/cadastro')
def cadastro():
  return render_template('PaginaCadastroUser.html')
@app.route('/ajuda')
def ajuda():
  return render_template('ajuda.html')

@app.route('/cadastrovend')
def cadastrovend():
  return render_template('PaginaCadastroVendedor.html')
    
# if __name__ == '__main__':
#   app.run(debug=True)


@app.route('/', methods=['POST','GET'])



#telacliente= firebase.put('marmitech-1b071',{dictcliente})
#telavendedor= firebase.post('marmitech-1b071',{dictvendedores})

#validar trabalha com autenticação dos dados de cadrastro, percorrendo a base de dados e autenticando para fazer o login
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
#(incompleto)pagina inicial do usuario contento seus pedidos que estão armazenados no firebase retornando para o html
# def perfil():
# 	usuario=request.args['usuario']
# 	pedidototal=request.args['pedidototal']
# 	nomedapessoa=Marmitech.get('marmitech-1b071','-Kl_awU2thszeeh9okfl',None)
# 	return render_template('')

#função que retorna a pagina inicial
def home():
    usuario=request.args['usuario']

    return render_template('PaginaHome.html', nomedapessoa=usuario) 
 # inicia o programa
if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0', port=5000) 