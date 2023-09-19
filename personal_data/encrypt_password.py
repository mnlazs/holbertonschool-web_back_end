#!/usr/bin/env python3
"""Funtion"""
import bcrypt


def hash_password(password: str) -> bytes:
    """funcion que recibe un argumento password y retorna salted"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ recibe dos argumentos y retorna un boolen"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password())
