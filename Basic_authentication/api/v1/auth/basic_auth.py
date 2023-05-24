#!/usr/bin/env python3
"""basic auth class"""
from .auth import Auth
import re
import base64


class BasicAuth(Auth):
    """basic auth class inherits from auth"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:  # noqa
        """extracts the auth header"""
        if authorization_header is None or type(authorization_header) != str:
            return None
        if not re.search('^Basic ', authorization_header):
            return None
        return re.sub('^Basic ', '', authorization_header)

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:  # noqa
        """returns the decoded value of a Base64 string"""
        if base64_authorization_header is None or type(base64_authorization_header) != str:  # noqa
            return None

        try:
            return base64.b64decode(base64_authorization_header).decode('utf-8')  # noqa
        except Exception:
            return None
