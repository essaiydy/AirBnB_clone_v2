#!/usr/bin/python3
'''a script that starts a Flask web application'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''function display display “Hello HBNB!”'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    '''function display display “HBNB”'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    '''function display a text'''
    return "C {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
