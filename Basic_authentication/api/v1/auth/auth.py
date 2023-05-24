#!/usr/bin/env python3
"""holds an auth class"""
from flask import request
from typing import List, TypeVar


class Auth():
    """an authorization class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """auth auth auth"""
        return False

    def authorization_header(self, request=None) -> str:
        """header header header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """user user user"""
        return None
