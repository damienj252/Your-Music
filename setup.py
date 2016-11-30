import sqlite3

DATABASE = 'data/music.db'


conn = sqlite3.connect('data/music.db')

#Creates database if it has not already been set up.
def setup_db():
    db = sqlite3.connect(DATABASE)
    cur = db.cursor()

    # Create the table if it doesn't exist.
    cur.execute("CREATE TABLE IF NOT EXISTS musicTable(artist TEXT , song TEXT)")
    db.commit()

    # Insert some dummy data if the table is empty.
    cur.execute("SELECT COUNT(*) FROM musicTable")
    if cur.fetchall()[0][0] == 0:
        cur.execute('INSERT INTO musicTable(artist, song) VALUES("Eminem", "Monsters")')
        cur.execute('INSERT INTO musicTable(artist, song) VALUES("Lost Frequencies", "Are you with me")')

    db.commit()

if __name__ == "__main__":
  setup_db()