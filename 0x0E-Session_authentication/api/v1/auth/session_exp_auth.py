#!/usr/bin/env python3
""" Class that inherits from SessionAuth"""

from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """Add an expiration date to a Session ID"""
    def __init__(self):
        """Overload init method"""
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Overload create_session method"""
        try:
            session_id = super().create_session(user_id)
        except Exception:
            return None
        session_dictionary = {
                'user_id': user_id, 'created_at': datetime.now()
                }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Overload user_id_for_session_id method"""
        if session_id is None:
            return None
        if self.user_id_by_session_id.get(session_id) is None:
            return None
        if 'created_at' not in self.user_id_by_session_id.get(session_id):
            return None
        if self.session_duration <= 0:
            return (self.user_id_by_session_id.get(session_id)).get('user_id')
        if (self.user_id_by_session_id.get(session_id)).get(
                'created_at') + timedelta(
                seconds=self.session_duration) < datetime.now():
            return None
        else:
            return (self.user_id_by_session_id.get(session_id)).get('user_id')
