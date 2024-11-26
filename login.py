import sqlite3
class Login():

    def __init__(self):
        self.user_name = input("enter your nickname ")
        self.__password = input("enter your password ")

    def get_password (self):
        return self.__password
    

class CheckDBLog(Login): #перевірка бд на наявність коримтувача з підтвердженням

    def __init__(self):
        super().__init__()
        self.is_authenticated = False
        self.user_in_sn = None
    
    def check_user_exists(self):

        conn = sqlite3.connect('social_network.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Users WHERE user_name = ? AND password = ? ",
                       (self.user_name, self.get_password() ))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            self.is_authenticated = True
            self.user_in_sn = self.user_name
        else:
            print("incorrect user name or password.")