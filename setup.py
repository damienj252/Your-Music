import sqlite3

DATABASE = 'data/data.db'

def setup_db():
#Creates database if it has not already been set up.
  db = sqlite3.connect(DATABASE)
cur = db.cursor()

# Create the table if it doesn't exist.
  cur.execute("CREATE TABLE IF NOT EXISTS mytable(id INTEGER PRIMARY KEY, name TEXT)")
    db.commit()

#Insert some dummy data if the table is empty.
  cur.execute("SELECT COUNT(*) FROM mytable")
    if cur.fetchall()[0][0] == 0:
    cur.execute('INSERT INTO mytable(artist) VALUES("Ian")')
    db.commit()

if __name__ == "__main__":
setup_db()