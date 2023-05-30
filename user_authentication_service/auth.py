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

    def create_session(self, email: str) -> str:
        """creates a session id for a user based on their email"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str):
        """gets a user from the db by session id"""
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """updates a users session id to None"""
        self._db.update_user(user_id, session_id=None)


def _hash_password(password: str) -> bytes:
    """hashes a password"""
    salt = bcrypt.gensalt()
    bytes = password.encode('utf-8')
    return bcrypt.hashpw(bytes, salt)


def _generate_uuid() -> str:
    """creates an id"""
    return str(uuid4())
