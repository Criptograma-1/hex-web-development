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
