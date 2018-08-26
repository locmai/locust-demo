from flask import Flask, request, jsonify, app, render_template
import time
import random

app = Flask(__name__)


@app.route('/api', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return jsonify(method=request.method)
    return jsonify(method=request.method,payload=request.json)


@app.route('/flaky')
def flaky():
    x = random.randint(0, 1)
    return render_template('flaky.html', flaky_val=x)


if __name__ == '__main__': 
    app.run(host='0.0.0.0')
