#!/usr/bin/env python3
"""Print log message obfuscated"""

from typing import List
import re


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """Function that use a regex to replace occurrences of certain field values
       Args:
            -fields: a list of strings representing all fields to obfuscate.
            -redaction: a string representing by what the field will be obfuscated
            -message: a string representing the log line
            -separator: a string representing by which character is separating all
                        fields in the log line (message).
       Return:
            -the log message obfuscated
    """
    for i in fields:
        message = re.sub(fr'{i}=.+?{separator}',
                         f'{i}={redaction}{separator}',
                         message)
        return message
