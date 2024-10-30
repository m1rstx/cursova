import sqlite3 
import datetime

class Post():
    
    def __init__ (self):
        self.title = input("enter title for post >>> ")
        self.text = input("enter your post text >>> ")
        self.datetime = datetime.datetime.now()

#     def introduce(self):
#         print(f"""      {self.title}
# {self.text}\n
# post time: {self.datetime}""")

class Post_DB(Post):

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

post_db = Post_DB()
post_db.save_to_db()