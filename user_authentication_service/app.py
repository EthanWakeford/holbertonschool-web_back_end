#!/usr/bin/env python3
"""flask app"""
from os import getenv
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def root():
    """root of flask app"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
