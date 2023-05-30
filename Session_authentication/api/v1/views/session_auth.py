#!/usr/bin/env python3
""" Module of session_auth views"""
from flask import jsonify, abort, make_response, request
from api.v1.views import app_views
from os import getenv
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """runs session authentication"""
    email = request.form.get('email')
    if not email:
        return jsonify({ "error": "email missing" }), 400
    
    password = request.form.get('password')
    if not password:
        return jsonify({ "error": "password missing" }), 400

    users = User.search({'email': email})
    if len(users) == 0:
        return jsonify({ "error": "no user found for this email" }), 404
    user = users[0]

    if not user.is_valid_password(user_pwd):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth

    session_id = auth.create_session(user.id)
    user_info = user.to_json()
    response = jsonify(user_info)

    cookie = getenv('SESSION_NAME')
    response = make_response(response)
    response.set_cookie(cookie, session_id)

    return response
