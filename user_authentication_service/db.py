#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User


class DB:
    """DB class
    """
    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Agrega un nuevo ususario a la base de datos y retorna el object."""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """ This method takes in arbitrary keyword arguments and
        returns the first row found in the users table as
        filtered by the method’s input arguments. No validation
        of input arguments required at this point. """
        if not kwargs:
            raise InvalidRequestError
        users_columns = [
            'id',
            'email',
            'hashed_password',
            'session_id',
            'reset_token'
        ]
        for arg in kwargs:
            if arg not in users_columns:
                raise InvalidRequestError

        """ search table for user """
        search_user = self.__session.query(User).filter_by(**kwargs).first()

        if search_user:
            return search_user
        else:
            raise NoResultFound
