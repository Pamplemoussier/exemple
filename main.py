from flask import Flask

app = Flask(__name__)

# Page d'accueil
@app.route('/')
def index():
  return "Hello World !"

app.run(host='0.0.0.0', port=81)