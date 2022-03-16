#!/usr/bin/env python3
"""Print log message obfuscated"""

from typing import List
import re
import logging

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Constructor"""
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """Method to filter values in incoming log records"""
        return filter_datum(self.fields,
                            self.REDACTION,
                            super().format(record),
                            self.SEPARATOR)


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """Method that use a regex to replace occurrences of certain field values
       Args:
            -fields: a list of strings representing all fields to obfuscate.
            -redaction: a string representing by what the field will
                        be obfuscated
            -message: a string representing the log line
            -separator: a string representing by which character is
                        separating all fields in the log line (message).
       Return:
            -the log message obfuscated
    """
    for i in fields:
        message = re.sub(fr'{i}=.+?{separator}',
                         f'{i}={redaction}{separator}',
                         message)
    return message


def get_logger() -> logging.Logger:
    """Hide important PIIs or information in logs
        Return:
            -a logging.Logger object
    """
    logger = logging.getLogger("user_data")
    handler = logging.StreamHandler()
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger

