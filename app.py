import json
import time
from flask import Flask, Response, render_template, after_this_request
import codecs #unicode

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
        return json.dumps({id:data[id]}, ensure_ascii=False)
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
        return json.dumps(data['id'], ensure_ascii=False)
    else:
        return "404"


def loadJSON():
    data = codecs.open("PISDATA.json", "r", "utf-8").read()
    return json.loads(data)

