import sqlite3
from datetime import datetime

# Connect to the database
conn = sqlite3.connect('blog.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    joined_date DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    posted_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY,
    post_id INTEGER,
    user_id INTEGER,
    content TEXT NOT NULL,
    commented_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(post_id) REFERENCES posts(id),
    FOREIGN KEY(user_id) REFERENCES users(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS tags (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS post_tags (
    post_id INTEGER,
    tag_id INTEGER,
    FOREIGN KEY(post_id) REFERENCES posts(id),
    FOREIGN KEY(tag_id) REFERENCES tags(id),
    PRIMARY KEY(post_id, tag_id)
)
''')
conn.commit()

# Insert a user, a post, a comment, and associate tags with the post
cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ("alice", "alice@example.com"))
cursor.execute("INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)", (1, "My First Post", "This is the content of my first post!"))
cursor.execute("INSERT INTO comments (post_id, user_id, content) VALUES (?, ?, ?)", (1, 1, "This is a self-comment on my own post!"))
cursor.execute("INSERT INTO tags (name) VALUES (?)", ("Introduction",))
cursor.execute("INSERT INTO post_tags (post_id, tag_id) VALUES (?, ?)", (1, 1))
conn.commit()

# Query to get all posts of a user along with their tags
cursor.execute('''
SELECT posts.title, tags.name
FROM posts
JOIN post_tags ON posts.id = post_tags.post_id
JOIN tags ON post_tags.tag_id = tags.id
WHERE posts.user_id = ?
''', (1,))

user_posts_with_tags = cursor.fetchall()
for post in user_posts_with_tags:
    print(f"Post Title: {post[0]} - Tag: {post[1]}")

conn.close()
