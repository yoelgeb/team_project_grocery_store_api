from product_database import *

db_curser = my_connection.cursor()

print("Welcome to our Grocery Store!")
def create_account():
    while True:
        create_account = input("Would you like to create an account?Y/N: ")
        create_account = create_account.lower()
        if(create_account != "y"):
            break
        else:
            first_name = input("What is first name: ")
            email=input("What is your email?: ")
            password=input("What is your password?: ")
            print(create_user(first_name, email, password))
            print("Account created")
        print(create_user())
def read_account():
    while True:
        view_account= input("Would you like to view your account? ")
        view_account = view_account.lower()
        if view_account != "y":
            break
        else:
            email = input("What is your email address? ")
            db_cursor.execute("""select email from customers""")
            email_db = db_cursor.fetchall()
            email_db = [item for t in email_db for item in t] 
            db_cursor.execute("""select customer_pass from customers""")
            password = db_cursor.fetchall()
            password_db = [item for t in password for item in t]  
            if email in email_db:
                password= input("What is your passowrd? ")
                if password in password_db:
                    print(f"Welcome {email}")
                    break
                else:
                    print("Wrong Password! Try Again")
                    continue
            else:
                print("Email do not exist!")
                continue
            print("Thank you for shopping")



def update_account():
    pass
def delete_account():
    pass
def buy():
    pass
def review():
    pass