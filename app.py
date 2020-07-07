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
    return json.dumps( GetPISdata(id) , ensure_ascii=False)
    

# @app.route('/pis/moduli/<id>')
# def pisModuliData(id):
#     @after_this_request
#     def add_header(response):
#         response.headers.add('Access-Control-Allow-Origin', '*')
#         return response
#     data = loadJSON()['MODULI']
#     if id in data:
#         return json.dumps(data['id'], ensure_ascii=False)
#     else:
#         return "404"


def GetPISdata(id):
    json = loadJSON()
    data = []
    opis = 'None'
    if id == 'IPS':
        data = json['IPS']
    else :
        if id in json['MODULI']: 
            data = json['MODULI'][id]
        elif id in json['PODMODULI']:
            data = json['PODMODULI'][id]
        elif id in json['APLIKACIJE']:
            data = json['APLIKACIJE'][id]
    if id in json['OPIS']:
        opis = json['OPIS'][id]
    return { 'data':data,'opis':opis }

def loadJSON():
    data = codecs.open("PISDATA.json", "r", "utf-8").read()
    return json.loads(data)

GetPISdata('Upravljanje trajnom poslovnom imovinom')