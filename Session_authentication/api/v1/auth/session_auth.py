#!/usr/bin/env python3
"""holds a class for session auth"""
from .auth import Auth
import re
import base64
from models.user import User
from typing import TypeVar


class SessionAuth(Auth):
    """controls session auth methods"""
    