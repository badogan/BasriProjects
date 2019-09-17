'''
Main route calls a function inside a class that is not in the same dir.
The class called is BasriNumbers
The function in class BasriNumbers is MultiplyThem
The class (and its functions) reside in a file called HelloWorldRoute.py
I modified the function inside the class so that it returns str. Apparently that's how Flusk works!
'''

import lib.HelloWorldRoute as h
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():   
    return h.BasriNumbers(4,8).MultiplyThem()

@app.route('/AddTheNumbers')
def AddTheNumbersCode():
    return 'Inside AddTheNumbersCode function!'

@app.route('/MultiplyTheNumbers')
def MultiplyTheNumbersCode():
    return 'Inside MultiplyTheNumbersCode function!'

if __name__ == '__main__':
    app.run()
