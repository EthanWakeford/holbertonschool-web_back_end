#!/usr/bin/env python3
"""holds a class for session auth"""
from .auth import Auth
import re
import base64
from models.user import User
from typing import TypeVar
from uuid import uuid4


class SessionAuth(Auth):
    """controls session auth methods"""
    user_id_by_session_id = {}


    def create_session(self, user_id: str = None) -> str:
        """creates a session id for user"""
        if type(user_id) != str:
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id
