from flask import Flask

app = Flask(__name__)

@app.route('/directeam', methods=['GET'])
def hello_world():
    return "I'm alive!"

@app.route('/')
def display_error():
    return "Error! Wrong request"