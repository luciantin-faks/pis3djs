import json
import time
from flask import Flask, Response, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pis')
def chart_data():
    def generate_random_data():
        while True:
            json_data = json.dumps({'PIS':loadJSON()['PIS']})
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    return Response(generate_random_data(), mimetype='text/event-stream')






def loadJSON():
    with open('PISDATA.json', 'r') as dat:
        data=dat.read()
    return json.loads(data)