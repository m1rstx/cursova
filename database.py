import sqlite3

# Підключення до бази даних (створюється, якщо не існує)
conn = sqlite3.connect('social_network.db')
cursor = conn.cursor()

# Створення таблиці User
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name VARCHAR(20),
    first_name VARCHAR(15),
    last_name VARCHAR(15),
    email VARCHAR(20),
    password VARCHAR(15)
)
''')

# Створення таблиці Post
cursor.execute('''
CREATE TABLE IF NOT EXISTS Post (
    post_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    title TEXT,
    text TEXT,
    like_counter INTEGER,
    date TEXT,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
)
''')

# Створення таблиці Comments
cursor.execute('''
CREATE TABLE IF NOT EXISTS Comments (
    comm_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    text TEXT,
    date TEXT,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
)
''')

# Створення таблиці SocialNetwork
cursor.execute('''
CREATE TABLE IF NOT EXISTS SocialNetwork (
    socialnetwork_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    post_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (post_id) REFERENCES User(post_id)
)
''')

# Збереження змін та закриття з'єднання
conn.commit()
conn.close()


