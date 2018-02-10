#DataBases Soportadas
import psycopg2
import sqlite3

from datetime import *
from random import *


class DBSelector:
    def __init__(self,dbType,dbname, user, password, host):
        self.dbType=dbType
        self.dbname=dbname
        self.user=user
        self.password=password
        self.host=host

        if dbType=='psycopg2':
            self.connection = psycopg2.connect("dbname=forex user=postgres password=postgres host=localhost")
        if dbType=='sqlite3':
            self.connection = sqlite3.connect(self.dbname + '.db')
        if dbType==':memory:':
            self.connection = sqlite3.connect(':memory:')

        self.cursor = self.connection.cursor()

    def execute(self,query):
        result = self.cursor.execute(query)
        self.connection.commit()
        return result

    def close(self):
        self.cursor.close()
        self.connection.close()



