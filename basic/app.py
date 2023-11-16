import db

menu = """Please select any of the options below: 
        1) A new entry for today
        2) View past entries
        3) Wish to quit...?.
         
        ENter your choice:  """


def new_entry():
    content_to_be_added = input("Enter the data to be added: ")
    date = input("Enter the date: ")
    db.add_entry(content_to_be_added,date)

def get_result():
    for entry in db.view_entry():
            print(entry['date'],"--->",entry['content']) #in case of dictionary we can format strings
            print("\n")
            # print(entry,"\n") # this is in case of tuple

print("HI..Welcome")
db.create_table()
user_input = input(menu)
while( user_input!= '3'):
    if user_input == "1":
        new_entry()
    elif user_input == "2":
        get_result()
        
    else:
        print("No such option available...!")
    user_input = input(menu)

# db.delete_entry()
