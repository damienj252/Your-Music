#Author: Damien Joyce
#Date: 1/12/16
#Original source: https://github.com/data-representation/example-sqlite/blob/master/setup.py
#Tutorials/information gathered from: https://docs.python.org/2/library/sqlite3.html

import sqlite3

DATABASE = 'data/music.db'

conn = sqlite3.connect('data/music.db')

#Creates database if it has not already been set up.
def setup_db():
    db = sqlite3.connect(DATABASE)
    cur = db.cursor()

    # Creates the table if it doesn't exist.
    cur.execute("CREATE TABLE IF NOT EXISTS musicTable(artist TEXT , song TEXT)")
    db.commit()

    # Inserts some data if no data is present
    cur.execute("SELECT COUNT(*) FROM musicTable")
    if cur.fetchall()[0][0] == 0:
        cur.execute('INSERT INTO musicTable(artist, song) VALUES("Eminem", "Monsters")')
        cur.execute('INSERT INTO musicTable(artist, song) VALUES("Mack", "Neva")')

    conn.commit()
    
    conn.close()

if __name__ == "__main__":
    setup_db()