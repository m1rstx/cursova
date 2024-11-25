import sqlite3 
import datetime


class Post(): 

    def __init__ (self):
        self.title = input("enter title for post >>> ")
        self.text = input("enter your post text >>> ")
        self.datetime = datetime.date.today()

    def introduce(self):
        print(f"""
Title: {self.title}
Text: {self.text}
Date: {self.datetime}""")

class PostDB(Post): #запис посту у бд 

    def __init__(self, author):
        super().__init__()
        self.author = author

    def save_to_db(self):
        conn = sqlite3.connect('social_network.db')
        cursor = conn.cursor()
        date_str = self.datetime.isoformat()

        cursor.execute('''
        INSERT INTO Post (creator, title, text, date)
        VALUES (?, ?, ?, ?)
        ''', (self.author, self.title, self.text, date_str))

        conn.commit()
        conn.close()