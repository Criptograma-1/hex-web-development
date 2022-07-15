#!/usr/bin/env python3
""" Auth script """
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> str:
    """Returns a hashed password"""
    return hashpw(password.encode('utf-8'), gensalt())
