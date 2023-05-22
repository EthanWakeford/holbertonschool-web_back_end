#!/usr/bin/env python3
"""returns a log"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:  # noqa
    """filters the message and takes out info listed in the fields"""
    return re.sub(r'(' + '|'.join(fields) + r')=[^{}]+'.format(separator), r'\1={}'.format(redaction), message)  # noqa
