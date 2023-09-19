#!/usr/bin/env python3
"""
Tasks 0. Regex-ing
"""
import re
from typing import List
import logging


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    "retorna el mensaje sofuscado"
    return re.sub(r'(' + '|'.join(fields) + r')=[^' + separator + r']*',
                  f'\\1={redaction}', message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """Filtra los valores de los registros"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)
