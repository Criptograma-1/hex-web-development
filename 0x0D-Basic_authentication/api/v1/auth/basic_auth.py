#!/usr/bin/env python3
"""
class BasicAuth that inherits from Auth
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Inherits from Auth
    """
     def __init__(self) -> None:
         """
         Initialize the class
         """
         super().__init__()
