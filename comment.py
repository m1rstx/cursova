import sqlite3
import datetime

class Comment():

    def __init__(self):
        self.comment_text = input("enter your comment text >>> ")
        self.datetime = datetime.datetime.now()

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

comment = Comment_DB()
comment.save_to_db()