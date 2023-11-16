import psycopg2
import os
from dotenv import load_dotenv

# url ="postgres://yxuhlojj:hw97GI1WCcC9aKcFsxziAWPQ_MPHnOgY@rain.db.elephantsql.com/yxuhlojj"

load_dotenv()
url = os.environ['database_uri']
connection = psycopg2.connect(url)



def create_table():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("create table if not exists entries (id SERIAL PRIMARY KEY,username TEXT,content TEXT, date TEXT);")

def add_entry(username,content_to_be_added,date):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("Insert into entries(username, content, date) values (%s,%s,%s);",(username,content_to_be_added,date))
            connection.commit()
    

def view_entry():
    # result = cursor.execute("Select * from entries;")
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("Select * from entries;")
            return cursor.fetchall()
        
def search_user(user):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("Select * from entries where username = (%s);",(user,))
            return cursor.fetchall()

def delete_entry():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("Drop table entries;")
            cursor.execute("create table if not exists entries (id SERIAL PRIMARY KEY,username TEXT,content TEXT, date TEXT);")

