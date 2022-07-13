#!/usr/bin/env python3
"""Class that inherits from Auth
"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Sessioon Authentication"""
    user_id = None
