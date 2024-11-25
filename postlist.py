import sqlite3

class AllPost():
    @staticmethod
    def watch_all_post():
        conn = sqlite3.connect('social_network.db')
        cursor = conn.cursor()
        
        cursor.execute("""
                       SELECT Post.post_id,
                       Post.creator, 
                       Post.title, 
                       Post.text, 
                       Post.date FROM Post""")

        posts_with_users = cursor.fetchall()

        for post in posts_with_users:
            print(f"""Post: №{post[0]} / Author: {post[1]}
        Title: {post[2]}
        Text: {post[3]}
        Date: {post[4]}\n""")
    
        conn.close()