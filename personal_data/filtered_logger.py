#!/usr/bin/env python3
"""returns a log"""
import re


def filter_datum(fields, redaction, message, separator):
    """filters the message and takes out info listed in the fields"""
    return re.sub(r'(' + '|'.join(fields) + r')=[^{}]+'.format(separator), r'\1={}'.format(redaction), message)  # noqa
