#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User

DATA = ['id', 'email', 'hashed_password', 'session_id', 'reset_token']


class DB:

    def __init__(self):
        """init mathod"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Session method"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """add user to database
            - email (string): email of user
            - hashed_password (string): password of user
        Returns user created
        """
        if not email or not hashed_password:
            return
        user = User(email=email, hashed_password=hashed_password)
        session = self._session
        session.add(user)
        session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find user, method that takes as argument:
            - arbitrary keyword arguments
        Returns he first row found in the users table as
         filtered by the method’s input arguments
        """
        user = self._session.query(User).filter_by(**kwargs).first()
        if not user:
            raise NoResultFound
        return user
        
     def update_user(self, user_id: int, **kwargs):
         """Update user
         Args:
             user_id (int): id of user
         """
         user = self.find_user_by(id=user_id)
         for key, val in kwargs.items():
             if key not in DATA:
                 raise ValueError
             setattr(user, key, val)
         self._session.commit()
         return None
