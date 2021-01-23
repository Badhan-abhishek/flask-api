import json
from flask import Flask, jsonify
# from flask_restful import Api
import json

data = json.load(open('data.json', 'r'))

app = Flask(__name__)
# app = Api(app)


@app.route('/')
def index():
    return jsonify(data)


app.run()
