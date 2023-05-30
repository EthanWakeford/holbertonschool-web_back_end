#!/usr/bin/env python3
"""does some authenticating"""
import bcrypt
import base64
from db import DB
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """adds a user into the db"""
        db = DB()

        try:
            db.find_user_by(email=email)
            # print('found me a user')
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            # print("no results")
            hashed_password = _hash_password(password)
            db.add_user(email, hashed_password)
            user = db.find_user_by(email=email)
            # print(user.id, user.email)
        
        return User


def _hash_password(password: str) -> bytes:
    """hashes a password"""
    salt = bcrypt.gensalt()
    bytes = password.encode('utf-8')
    return bcrypt.hashpw(bytes, salt)
