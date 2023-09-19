#!/usr/bin/env python3
"""Funtion"""
import bcrypt


def hash_password(password: str) -> bytes:
    """funcion que recibe un argumento password y retorna salted"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
