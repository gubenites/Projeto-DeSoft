from flask import Flask, render_template
  
app = Flask(__name__)
  
@app.route('/')
def home():
  return render_template('PaginaHome.html')
  
@app.route('/cadastro')
def cadastro():
  return render_template('PaginaCadastroUser.html')

@app.route('/cadastrovend')
def cadastrovend():
  return render_template('PaginaCadastroVendedor.html')
    
if __name__ == '__main__':
  app.run(debug=True)