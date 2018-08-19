from flask import Flask
from flask import render_template
import socket
socket.gethostbyname("")

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# @app.route('/')
# def home():
#     return render_template('index.html')
