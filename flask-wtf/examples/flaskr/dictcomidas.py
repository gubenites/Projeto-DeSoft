from firebase import firebase

Marmitech = firebase.FirebaseApplication('https://marmitech-1b071.firebaseio.com/')
listaVendedores = []
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



#telacliente= firebase.put('marmitech-1b071',{dictcliente})
#telavendedor= firebase.post('marmitech-1b071',{dictvendedores})


listasenha = []
listausuario=[]

cli=Vendedor(1234)
#vend = Vendedor('Antonio',"antonio@hotmail.com","1234")
listasenha.append(cli)
caarlho=Vendedor(helio)
listausuario.append(caarlho)
#vend = Vendedor("joao","joao@hotmail.com","12345")
# listaVendedores.append(vend)
telavendedor=Marmitech.post('marmitech-1b071',listasenha[0].SalvarVendedor())

telavendedor = Marmitech.post('marmitech-1b071',listausuario[0].SalvarVendedor())


print (telavendedor)


# app = Flask(__name__, static_url_path='')

# UPLOAD_FOLDER = 'static/uploads/'
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

# app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
    
# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    
                             
# @app.route('/', methods=['POST','GET'])

# teste = Marmitech.get('-Kl_awU2thszeeh9okfl', 'antonio')
# print(teste)		
# def validacao():
# 	if.request.mthod== 'POST':
# 		nomedapessoa.request.form['nomedapessoa']
# 		senha=request.form['senha']
# ler=Marmitech.get('-Kl_awU2thszeeh9okfl',None)
# print (ler)