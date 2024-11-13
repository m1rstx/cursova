import sqlite3
import datetime

class Comment():

    def __init__(self):
        self.comment_text = input("enter your comment text >>> ")
        self.datetime = datetime.datetime.now()

    def introduce(self):
        print(f"""{self.comment_text}\n
comment time: {self.datetime}""")
class Comment_DB(Comment):

    def save_to_db(self):
        conn = sqlite3.connect('social_network.db')
        cursor = conn.cursor()
        date_str = self.datetime.isoformat()

        cursor.execute('''
        INSERT INTO Comments (text, date)
        VALUES (?, ?)
        ''', (self.comment_text, date_str))

        conn.commit()
        conn.close()