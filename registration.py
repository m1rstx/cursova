import sqlite3

class Registration():

    def __init__ (self):
        self.user_name = input("enter your nickname ")
        self.first_name = input("enter your first_name ")
        self.last_name = input("enter your last_name ")
        self.__email = input("enter your email ")
        self.__password = input("enter your password ")

    def get_email (self):
        return self.__email

    def get_password (self):
        return self.__password

class Reg_DB(Registration):

    def save_to_db(self):
        conn = sqlite3.connect('social_network.db')
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO Users (user_name, first_name, last_name, email, password)
        VALUES (?, ?, ?, ?, ?)        
        ''', (self.user_name, 
                self.first_name, 
                self.last_name, 
                self.get_email(), 
                self.get_password())
        )

        conn.commit()
        conn.close()


