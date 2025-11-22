import sqlite3

conn = sqlite3.connect("posted.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    link TEXT UNIQUE
)
""")

conn.commit()

def has_been_posted(link):
    cursor.execute("SELECT 1 FROM posts WHERE link = ?", (link,))
    return cursor.fetchone() is not None

def mark_as_posted(link):
    cursor.execute("INSERT OR IGNORE INTO posts (link) VALUES (?)", (link,))
    conn.commit()
