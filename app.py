#Author: Damien Joyce
#Date: 30/11/16
#Original source: https://github.com/data-representation/example-project


import flask as fl
import sqlite3

DATABASE = 'data/music.db'

app = fl.Flask(__name__)

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/artist", methods=["GET", "POST"])
def artist():
    artist = (fl.request.values["artistinput"])
    return artist

@app.route("/song", methods=["GET", "POST"])
def song():
    song = (fl.request.values["songinput"])
    return song
if __name__ == "__main__":
    app.run()
#---------------------------------------------------------------------
#---------------------------------------------------------------------
    
def get_db():
    db = getattr(fl.g, '_database', None)
    if db is None:
        db = fl.g._database = sqlite3.connect(DATABASE)
        return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(fl.g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello():
    cur = get_db().cursor()
    cur.execute("SELECT artist, song FROM musicTable") 
    return str(cur.fetchall())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    app = fl.Flask(__name__)

