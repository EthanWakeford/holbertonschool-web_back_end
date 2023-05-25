#!/usr/bin/env python3
"""returns a log"""
import re
from typing import List, Tuple
import logging


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:  # noqa
    """filters the message and takes out info listed in the fields"""
    return re.sub(r'(' + '|'.join(fields) + r')=[^{}]+'.format(separator), r'\1={}'.format(redaction), message)  # noqa


def get_logger() -> logging.Logger:
    """returns a logger object"""
    logger = logging.Logger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(list(PII_FIELDS))
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


PII_FIELDS: Tuple = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """formats a log message"""
        log_message: str = super().format(record)
        return filter_datum(self.fields, self.REDACTION, log_message, self.SEPARATOR)  # noqa
