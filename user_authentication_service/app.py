#!/usr/bin/env python3
"""flask app"""
from os import getenv
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
from auth import Auth


AUTH = Auth()

app = Flask(__name__)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.route('/', methods=['GET'])
def root():
    """root of flask app"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """registers a user"""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
