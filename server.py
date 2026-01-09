from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.routep('/index')


def index():
    return "Hello World"

if __name__ == "__main__":
    serve(app, host = '0.0.0.0', port = 8000)
    
    
    
    
    
    
    
    
    
### --------> Server is also commonly known as main.py
'''
from flask import Flask, request, render_template'''