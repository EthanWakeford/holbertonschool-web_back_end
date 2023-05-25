#!/usr/bin/env python3
"""encrypts passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hashes a password"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """evaluates whether a hashed password matches given password"""
    return bcrypt.checkpw(password.encode(), hashed_password)
