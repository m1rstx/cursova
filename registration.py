import sqlite3
import re
class Registration():

    def __init__ (self):
        self.user_name = input("enter your nickname ")
        self.first_name = input("enter your first_name ")
        self.last_name = input("enter your last_name ")
        self.__email = input("enter your email ")

        while not self.is_valid_email(self.__email):
            print("Invalid email format. Please try again.")
            self.__email = input("Enter a valid email: ")

        self.__password = input("enter your password ")

    def get_email (self):
        return self.__email

    def get_password (self):
        return self.__password
    
    @staticmethod
    def is_valid_email(email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

class RegDB(Registration): # запис користувача до бд 

    def is_email_unique(self):
        conn = sqlite3.connect('social_network.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Users WHERE email = ?", (self.get_email(),))
        user = cursor.fetchone()
        conn.close()

        return user is None

    def save_to_db(self):
        if not self.is_email_unique():
            print("This email is already registered. Please use a different email.")
            return

        conn = sqlite3.connect('social_network.db')
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO Users (user_name, first_name, last_name, email, password)
        VALUES (?, ?, ?, ?, ?)
        ''',(self.user_name,
                self.first_name,
                self.last_name,
                self.get_email(),
                self.get_password()))

        conn.commit()
        conn.close()