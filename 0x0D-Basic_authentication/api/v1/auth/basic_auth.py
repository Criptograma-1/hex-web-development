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


    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """
        Returns the Base64 part of the Authorization
        header for a Basic Authentication
        """
        if authorization_header is None:
            return None
        elif type(authorization_header) is not str:
            return None
        elif authorization_header[:6] != "Basic ":
            return None
        else:
            return authorization_header.split(" ")[1]
