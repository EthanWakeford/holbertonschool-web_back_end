#!/usr/bin/env python3
"""returns a log"""
import re
from typing import List, Tuple
import logging
import mysql.connector
from mysql.connector import errorcode
import os


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connect to the MySQL database using the credentials from environment
    variables.

    Returns:
        mysql.connector.connection.MySQLConnection: The connection to the
        MySQL database.

    """
    username = os.environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.environ.get("PERSONAL_DATA_DB_NAME")

    try:
        db = mysql.connector.connect(
            user=username,
            password=password,
            host=host,
            database=db_name
        )
        return db
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Invalid credentials.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print("Error: Failed to connect to the database.")
        raise


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:  # noqa
    """filters the message and takes out info listed in the fields"""
    return re.sub(r'(' + '|'.join(fields) + r')=[^{}]+'.format(separator), r'\1={}'.format(redaction), message)  # noqa


def get_logger() -> logging.Logger:
    """returns a logger object"""
    logger = logging.getLogger('user_data')
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
