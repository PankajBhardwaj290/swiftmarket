import os
import pymysql.cursors
from dotenv import load_dotenv
import pandas as pd 

load_dotenv()

host = os.getenv('HOST')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
database = os.getenv('DATABASE')

connection = pymysql.connect(user=user,
host = host,
password =password,
database =database)

cursor = connection.cursor()

def select_query(query):
    
    cursor.execute(query)
    rows = cursor.fetchall()
    df = pd.DataFrame(data=rows,columns=[column[0] for column in cursor.description])
    
    return df

def show_talbes():
    query = 'show_tables;'
    cursor.execute(query)
    rows = cursor.fetchall()
    df = pd.DataFrame(data=rows,columns=[column[0] for column in cursor.description])
    
    return df