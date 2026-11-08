import sqlite3

DB = "bot.db"


def init():
    conn = sqlite3.connect(DB)
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, coins INTEGER, xp INTEGER)")
    conn.execute("CREATE TABLE IF NOT EXISTS usage (user_id INTEGER, command TEXT)")
    conn.commit()
    conn.close()


def get_user(user_id):
    conn = sqlite3.connect(DB)
    row = conn.execute("SELECT id, coins, xp FROM users WHERE id = ?", (user_id,)).fetchone()
    conn.close()
    return {"id": row[0], "coins": row[1], "xp": row[2]} if row else None
