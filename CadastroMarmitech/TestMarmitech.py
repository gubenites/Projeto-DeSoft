from flask import flask , render_template, request, url_for, redirect, send_from_directory
import os
import random
from firebase import firebase

Marmitech=firecall.Firebase("https://marmitech-db32e.firebaseio.com/")
EMAIL=[]
USER=[]
class Pessoa():

    def __init__(self, usuario, email, senha):
        self.usuario = usuario
        self.email = email
        self.senha = senha
        self.dict = {}

    def salvarPessoa(self):
        self.dict[self.email]=self.usuario,self.email,self.senha
        EMAIL.append(self.email)
        return self.dict

        Marmitech.put_sync(point="/Pessoas/{0}".format(self.usuario),data=self.dict)

@app.route('/login', methods = ['POST','GET'])

def firstpage():
      #LOGIN
  if request.method == 'POST': #Quando o método for POST
    usuario = request.form['usuario'] #Recebe usuario do HTML
    senha = request.form['senha']  #Recebe senha do HTML
    L = eval(Marmitech.get_sync(point="/Lista-de-Usuarios")) #Chama Lista de Usuarios do FireBase
    #Validação do login:
    if usuario in L:
        listasenha=[]
        s= eval(Marmitech.get_sync(point="/usuario/{0}/senha".format(usuario)))
        listasenha.append(s)
        if senha in listasenha:
            return render_template('escolhecomida.html', usuario=usuario)#HOME pós login 
    else:
        e = 'Usuário ou senha inválido'
        return render_template('mainerro.html', usuario=usuario, dic = Marmitech.get_sync(point="/usuarios/{0}".format(usuario)), erro = e)
 
  return render_template('main.html', usuario = usuario('','','',''))        
  
      


@app.route('/cadastro', methods=['POST','GET'])

def conta():
    #CADASTRO DO USUÁRIO
    if request.method == 'POST':
      
        nomecompleto = request.form['pessoa'] #Recebe pessoa do HTML como nome
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
            Marmitech.put_sync(point="/Lista-de-Usuarios/{0}".format(usuario),data = usuario) # Lista de usuario              
            return render_template('home.html', dic = USER[-1].usuario, usuario = usuario)
        for p in use:        
            usemail = eval(Marmitech.get_sync(point = "/Pessoas/{0}/email".format(p)))
            mail.append(usemail)
 
    return render_template('login.html', erro = '')
      
