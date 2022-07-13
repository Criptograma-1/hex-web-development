#!/usr/bin/env python3
"""Class SessionDBAuth that inherits from SessionExpAuth"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from os import getenv


class SessionDBAuth(SessionExpAuth):
    """Class SessionDBAuth"""
    def create_session(self, user_id=None):
        """Creates and stores new instance
        of UserSession and returns the Session ID"""
        pass

    def user_id_for_session_id(self, session_id=None):
        """Returns the User ID by requesting UserSession
        in the database based on session_id"""
        if session_id is None or type(session_id) is not str:
            return None
        else:
            pass

    def destroy_session(self, request=None):
        """destroys the UserSession based on
        the Session ID from the request cookie"""
        pass
