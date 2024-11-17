import sqlite3 
import datetime

class Post(): 

    def __init__ (self):
        self.title = input("enter title for post >>> ")
        self.text = input("enter your post text >>> ")
        self.datetime = datetime.date.today()

    def introduce(self):
        print(f"""\nTitle: {self.title}
Text: {self.text}\n
Date: {self.datetime}""")

class Post_DB(Post): #запис посту у бд 

    def save_to_db(self):
        conn = sqlite3.connect('social_network.db')
        cursor = conn.cursor()
        date_str = self.datetime.isoformat()

        cursor.execute('''
        INSERT INTO Post (title, text, date)
        VALUES (?, ?, ?)
        ''', (self.title, self.text, date_str))

        conn.commit()
        conn.close()