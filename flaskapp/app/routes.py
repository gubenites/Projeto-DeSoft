from flask import Flask, render_template
from firebase import firebase
from flask import Flask
from .forms import FirePut
app = Flask(__name__)
firebase = firebase.FirebaseApplication("<https://marmitech-1b071.firebaseio.com>", None)
 
@app.route('/')
def home():
  return render_template('home.html')
@app.route('/about')
def about():
  return render_template('about.html') 
if __name__ == '__main__':
  app.run(debug=True)