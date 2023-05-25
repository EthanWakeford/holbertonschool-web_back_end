#!/usr/bin/env python3
"""encrypts passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hashes a password"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password
