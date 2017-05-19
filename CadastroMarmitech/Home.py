import firecall

Marmitech=firecall.Firebase("https://marmitech-db32e.firebaseio.com/")
USER=[]
def firstpage():
      #LOGIN
  if request.method == 'POST': #Quando o método for POST
    usuario = request.form['usuario'] #Recebe usuario do HTML
    senha = request.form['senha']  #Recebe senha do HTML
    L = eval(Marmitech.get_sync(point="/Lista-de-Usuarios")) #Chama Lista de Usuarios do FireBase
    P = eval(Marmitech.get_sync(point="/Lista-de-Usuarios")) #Chama Lista de Senhas do FireBase
      #Validação do login:
    if usuario in L and senha in P:
      listasenha=[]
      s= eval(Marmitech.get_sync(point="/usuario/{0}/senha".format(usuario)))
      listasenha.append(s)
      if senha in listasenha:
        return render_template('escolhecomida.html', usuario=usuario)#HOME pós login
      else: 
        e = 'Senha incorreta'
                 
      return render_template('mainerro.html', usuario=usuario, dic = Marmitech.get_sync(point="/usuarios/{0}".format(usuario)), erro = e) 
    else:
      e = 'Usuário ou senha inválido'
      return render_template('mainerro.html', usuario=usuario, dic = Marmitech.get_sync(point="/usuarios/{0}".format(usuario)), erro = e)
 
  return render_template('main.html', usuario = usuario('','','',''))        
  
      
@app.route('/login', methods=['POST','GET'])

def conta():
    #CADASTRO DO USUÁRIO
  if request.method == 'POST':
      
    nome completo = request.form['pessoa'] #Recebe pessoa do HTML como nome
    usuario = request.form['usuario'] #Recebe usuario do HTML
    email = request.form['email'] #Recebe email do HTML
    senha = request.form['senha'] #Recebe senha do HTML
    use= eval(Marmitech.get_sync(point="/Lista-de-Usuarios")) #Chama Lista de usuarios do Firebase
    mail=[]        
  
    #condicoes:
    if usuario in use:
      e = 'Usuário já cadastrado'
      return render_template('loginrepetido.html', dic = Marmitech.get_sync(point="/Pessoas/{0}".format(nomepessoa)), erro = e)
    elif email in mail:
      e = 'Email já cadastrado'
      return render_template('loginemailrep.html', dic = Marmitech.get_sync(point="/Pessoas/{0}".format(nomepessoa)), erro = e)
    else:
      #Cadastra o novo usuário e manda as informações para o firebase
      USER.append(usuario)
      USER[-1] = Pessoa(usuario, email, senha)
      USER[-1].Salvar_Pessoa() 
      Marmitech.put_sync(point="/Lista-de-Usuarios/{0}".format(usuario),data=usuario) # Lista de usuario              
      return render_template('home.html', dic = USER[-1].usuario, usuario = usuario)
    for p in use:        
      usemail=eval(Marmitech.get_sync(point="/Pessoas/{0}/email".format(p)))
      mail.append(usemail)
 
  return render_template('login.html', erro = '')
      
  @app.route('/cadastro', methods=['POST','GET'])

def pedido():
  user=request.args['user']
  cao = request.args['cao']
  name=eval(PETinder.get_sync(point="/ListadogBR/{0}".format(cao)))
  file=eval(PETinder.get_sync(point="/ListadogBR/{0}/filename".format(cao)))
  return render_template('user.html', user=user,filename=file, cao=cao, name=name)
      
      
@app.route('/adotar', methods=['POST', 'GET'])