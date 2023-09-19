#!/usr/bin/env python3
import re
from typing import List
"""
Funtion filter_datum
"""

def filter_datum(fields, redaction, message, separator):
    return re.sub(r'(' + '|'.join(fields) + r')=[^' + separator + r']*', f'\\1={redaction}', message)
