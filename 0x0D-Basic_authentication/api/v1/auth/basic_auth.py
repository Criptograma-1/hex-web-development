#!/usr/bin/env python3
"""
class BasicAuth for basic authentication
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    A class that inherits from Auth
    """
     def __init__(self) -> None:
         """
         Initialize the class
         """
         super().__init__()
