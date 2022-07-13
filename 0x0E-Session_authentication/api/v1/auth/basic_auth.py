#!/usr/bin/env python3
"""
class BasicAuth for basic authentication
"""
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User
from models.base import DATA
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
        pass

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
        text_return = tuple(decoded_base64_authorization_header.split(":", 1))
        return text_return

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """
        returns the User instance based on his email and password.
        """
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        if not DATA:
            return None
        users_email = User.search({"email": user_email})
        if len(users_email) < 1:
            return None
        current_user = users_email[0]
        valid_password = current_user.is_valid_password(user_pwd)
        if valid_password:
            return current_user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        overloads Auth and retrieves the User instance for a request
        """
        auth_header = self.authorization_header(request)
        base64_auth = self.extract_base64_authorization_header(auth_header)
        base64_decoded = self.decode_base64_authorization_header(base64_auth)
        credentials = self.extract_user_credentials(base64_decoded)
        user_obj = self.user_object_from_credentials(
            credentials[0], credentials[1])
        return user_obj
