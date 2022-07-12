#!/usr/bin/env python3
"""
class BasicAuth for basic authentication
"""
from api.v1.auth.auth import Auth
import binascii
import base64


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


    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """
        returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        elif type(base64_authorization_header) is not str:
            return None
        try:
            base64_bytes = base64.b64decode(base64_authorization_header)
            base64_text = base64_bytes.decode('ascii')
            return base64_text
        except(binascii.Error, UnicodeDecodeError):
            return None


    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """
        returns the user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return(None, None)
        if type(decoded_base64_authorization_header) is not str:
            return(None, None)
        if ':' not in decoded_base64_authorization_header:
            return(None, None)
        text_return = decoded_base64_authorization_header.split(":")
        return(text_return[0], text_return[1])
