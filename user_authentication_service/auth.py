#!/usr/bin/env python3
"""does some authenticating"""
import bcrypt
import base64
from db import DB
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """adds a user into the db"""

        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            hashed_password = _hash_password(password)
            self._db.add_user(email, hashed_password)

        return User

    def valid_login(self, email: str, password: str) -> bool:
        """validates a password"""
        try:
            user = self._db.find_user_by(email=email)
            password = password.encode('utf-8')
            return bcrypt.checkpw(password, user.hashed_password)
        except Exception as e:
            return False


def _hash_password(password: str) -> bytes:
    """hashes a password"""
    salt = bcrypt.gensalt()
    bytes = password.encode('utf-8')
    return bcrypt.hashpw(bytes, salt)


def _generate_uuid() -> str:
    """creates an id"""
    return str(uuid4())
