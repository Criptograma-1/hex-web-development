#!/usr/bin/env python3
"""Print log message obfuscated"""

from typing import List
import re
import logging
import os
import mysql.connector

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


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Method to connect to the MySQL database
        Return:
            -a connector to the database
    """
    return mysql.connector.connect(
            host=os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost'),
            database=os.environ.get('PERSONAL_DATA_DB_NAME', 'root'),
            user=os.environ.get('PERSONAL_DATA_DB_USERNAME'),
            password=os.environ.get('PERSONAL_DATA_DB_PASSWORD', ''))


def main():
    """
    Obtain a database connection using get_db and retrieve all rows in
    the users table and display each row under a filtered format
    """
    database = get_db()
    cursor = database.cursor()
    curso.execute("SELECT * FROM users;")
    result = curso.fetchall()

    for row in result:
        message = f"name={row[0]}; " + \
                  f"email={row[1]}; " + \
                  f"phone={row[2]}; " + \
                  f"ssn={row[3]}; " + \
                  f"password={row[4]};"
        print(message)
        log_record = logging.LogRecord(
                "my_logger",
                logging.INFO,
                None, None, message,
                None, None)
        formatter = RedactingFormatter(PII_FIELDS)
        formatter.format(log_record)
    curso.close()
    database.close()


if __name__ == "__main__":
    main()
