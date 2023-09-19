#!/usr/bin/env python3
"""Funtion"""
import bcrypt


def hash_password(password: str) -> bytes:

    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
