#!/usr/bin/env python3
"""basic auth class"""
from .auth import Auth
import re
import base64
from models.user import User
from typing import TypeVar


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

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):  # noqa
        """returns the user email and password from the Base64 decoded value"""
        if decoded_base64_authorization_header is None or type(decoded_base64_authorization_header) != str:  # noqa
            return None, None
        if not re.search(':', decoded_base64_authorization_header):
            return None, None
        return tuple(re.split(':', decoded_base64_authorization_header))

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):  # noqa
        """returns the User instance based on his email and password"""
        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_pwd) != str:
            return None
        try:
            user = User.search({'email': user_email})
            if len(user) == 0 or not user[0].is_valid_password(user_pwd):
                return None
            return user[0]
        except KeyError:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """retrieves the User instance, checks for valid header"""
        auth_header = self.authorization_header(request)
        base64_auth_header = self.extract_base64_authorization_header(auth_header)  # noqa
        decoded_base64_authorization_header = self.decode_base64_authorization_header(base64_auth_header)  # noqa
        user_email, user_password = self.extract_user_credentials(decoded_base64_authorization_header)  # noqa
        return self.user_object_from_credentials(user_email, user_password)
