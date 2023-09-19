#!/usr/bin/env python3
"""
Tasks 0. Regex-ing
"""
import re
from typing import List
"""
Funtion filter_datum
"""


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    "retorna el mensaje sofuscado"
    return re.sub(r'(' + '|'.join(fields) + r')=[^' + separator + r']*',
                  f'\\1={redaction}', message)
