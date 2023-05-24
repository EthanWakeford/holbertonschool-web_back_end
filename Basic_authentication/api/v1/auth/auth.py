#!/usr/bin/env python3
"""holds an auth class"""
from flask import request
from typing import List


class Auth():
    """an authorization class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """auth"""
        return False

    def authorization_header(self, request=None) -> str:
        """header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """user"""
        return None
