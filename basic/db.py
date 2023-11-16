import sqlite3

entries = []


connection = sqlite3.connect("data.db")
connection.row_factory=sqlite3.Row  # without row factory the result will be a tuple this row factory is used to gt results in form of dictionary



def create_table():
    connection.execute("create table if not exists entries (content TEXT, date TEXT);")

def add_entry(content_to_be_added,date):
    
    connection.execute("Insert into entries values (?,?);",(content_to_be_added,date))
    connection.commit()
    # entries.append({"content":content_to_be_added,"date":date})
    # print(entries)

def view_entry():
    # result = connection.execute("Select * from entries;")
    result = connection.execute("Select * from entries where content='harini';")
    return result.fetchall()

def delete_entry():
    connection.execute("DELETE FROM entries;")
