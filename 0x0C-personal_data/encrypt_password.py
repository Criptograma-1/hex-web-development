#!/usr/bin/env python3
"""Encrypting passwords"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Method to encrypting passwords
        Args:
            -password: string to be encripted
        Return:
            -salted, hashed password, which is a byte string
    """
    hashed_password = bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Method to check if password is valid
        Args:
            -password: not ecrypted password
            -hashed_password: encrypted password
        Return:
            -True if passwords matches
            -False if passwords not matches
    """
    if bcrypt.checkpw(bytes(password, 'utf-8'), hashed_password):
        return True
    return False
