import os
import sqlite3

dirname = os.path.dirname(__file__)
connection = sqlite3.connect(os.path.join(dirname, 'database',"data.sqlite"))



def get_database_connection():
    return connection
    