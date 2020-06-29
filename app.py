import json
import time
from flask import Flask, Response, render_template, after_this_request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pis/<id>')
def pisData(id):
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    data = loadJSON()  # print(loadJSON()['IPS'])    
    if id in data:
        return json.dumps({id:data[id]})
    else:
        return "404"

@app.route('/pis/moduli/<id>')
def pisModuliData(id):
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    data = loadJSON()['MODULI']
    if id in data:
        return json.dumps(data['id'])
    else:
        return "404"


def loadJSON():
    with open('PISDATA.json', 'r') as dat:
        data=dat.read()
    return json.loads(data)

