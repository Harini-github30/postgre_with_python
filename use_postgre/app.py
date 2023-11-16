import db

menu = """Please select any of the options below: 
        1) A new entry for today
        2) View past entries
        3) To delete all the records.
        4) Search for a particular user
        5) Exit
         
        ENter your choice:  """

# load_dotenv()
# url = os.environ['database_uri']
# connection = psycopg2.connect(url)
def new_entry():
    username = input("Enter the name of the user")
    content_to_be_added = input("Data to be stored : ")
    date = input("date: ")
    db.add_entry(username,content_to_be_added,date)

def get_result():
    for entry in db.view_entry():
            print("ID: ",entry[0],"\n","Name: ",entry[1],"\n","Information: ",entry[2],"\n","Date: ",entry[3],"\n")
            # print(entry,"\n") # this is in case of tuple
            print("\n******************************\n")

def delete_table():
    confirm = input("Are you sure to delete all records?(y/n): ")
    if(confirm=='y' or confirm=='Y'): db.delete_entry()
    else: pass

def search(user):
     result = db.search_user(user)
     if not result:
          print("No entries for this user!")
     else:
          print("Infos' of the user {} :\n".format(user))
          i=1
          for d in result:
            print(i,")",d[2],"\nDate: ",d[3])
            i+=1
          print("\n")


    
print("HI..Welcome")
db.create_table()
print("\n****\n ")
user_input = input(menu)
while( user_input!= '5'):
    if user_input == "1":
        new_entry()
    elif user_input == "2":
        get_result()
    elif user_input=="3":
         delete_table() 
    elif user_input=="4":
         user = input("Enter the user name you need to search: ")
         search(user)
    else:
        print("No such option available...!")
    user_input = input(menu)

# db.delete_entry()
