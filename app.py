#Author: Damien Joyce
#Date: 1/12/16
#Original source: https://github.com/data-representation/example-project
#Tutorials/information gathered from: https://docs.python.org/2/library/sqlite3.html +
#https://www.fullstackpython.com/flask.html


import flask as fl
import sqlite3

DATABASE = 'data/music.db'

app = fl.Flask(__name__)
#---------------------------------------------------------------------
#---------------------------------------------------------------------
def get_db():
    db = getattr(fl.g, '_database', None)
    if db is None:
        db = fl.g._database = sqlite3.connect(DATABASE)
        return db
#---------------------------------------------------------------------
#---------------------------------------------------------------------
    
@app.route("/")
def root():
    return app.send_static_file('index.html')

#This allows the user insert the text (artist) into the database
@app.route("/artist", methods=["GET", "POST"])
def artist():
    artist = (fl.request.values["artistinput"])
    conn = sqlite3.connect('data/music.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO musicTable(artist) VALUES(?)", [artist])
    conn.commit()
    return artist

#This allows the user insert the text (song) into the database
@app.route("/song", methods=["GET", "POST"])
def song():
    song = (fl.request.values["songinput"])
    conn = sqlite3.connect('data/music.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO musicTable(song) VALUES(?)", [song])
    conn.commit() 
    return song

#This assigns information and requests for index.html
@app.route("/data", methods=["GET", "POST"])
def data():
    conn = sqlite3.connect('music.db')
    c = conn.cursor()
    # Create table
    c.execute("SELECT * from musicTable(artist, song)", (fl.request.form['artist']),(fl.request.form['song']) )
    return str(c.fetchall())

#---------------------------------------------------------------------
#---------------------------------------------------------------------

if __name__ == "__main__":
    app.run()

