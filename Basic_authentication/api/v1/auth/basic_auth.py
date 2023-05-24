#!/usr/bin/env python3
"""basic auth class"""
from .auth import Auth
import re


class BasicAuth(Auth):
    """basic auth class inherits from auth"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:  # noqa
        if authorization_header is None or type(authorization_header) != str:
            return None
        if not re.search('^Basic ', authorization_header):
            return None
        return re.sub('^Basic ', '', authorization_header)
