from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello My name is Naveen and I am a DevOps Engineer, TY!!!'
