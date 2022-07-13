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
        Return:
            - True if the path is not in the list of strings excluded_paths
            - False if the path is in the list of strings excluded_paths
        """
        if path is None or excluded_paths is None:
            return True

        if path in excluded_paths or f"{path}/" in excluded_paths:
            return False

        regex_excluded_paths = []

        for excluded_path in excluded_paths:
            if excluded_path[-1] == "*":
                regex_excluded_paths.append(excluded_path[:-1])
        for i in regex_excluded_paths:
            if i in path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns:
            - None if no header
            - request
        """
        if request is None or request.headers.get('Authorization') is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        returns None - request
        """
        return None
