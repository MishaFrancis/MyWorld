import os
from mysql import connector


def db_connect(self):
        conn = connector(
        user = os.getenv('user'),
        password = os.getenv('password'),
        host = os.getenv('host'),
        database = os.getenv('database'))
        print('A connection object has been created.')

