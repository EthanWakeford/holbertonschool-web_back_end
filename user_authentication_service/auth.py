#!/usr/bin/env python3
"""does some authenticating"""
import bcrypt
import base64


def _hash_password(password: str) -> bytes:
    """hashes a password"""
    salt = bcrypt.gensalt()
    bytes = password.encode('utf-8')
    return bcrypt.hashpw(bytes, salt)
