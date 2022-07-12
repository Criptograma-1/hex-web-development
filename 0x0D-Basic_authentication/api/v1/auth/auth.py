#!/usr/bin/env python3
"""
Auth class
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    A class to manage the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        returns False - path and excluded_paths
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        returns None - request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        returns None - request
        """
        return None
