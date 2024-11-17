import sqlite3

def watch_all_post():
        conn = sqlite3.connect('social_network.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT Post.post_id ,Post.title, Post.text, Post.date FROM Post")

        posts_with_users = cursor.fetchall()

        for post in posts_with_users:
            print(f" Post: №{post[0]}\n Title: {post[1]}\n Text: {post[2]}\n Date: {post[3]}\n")

        conn.close()