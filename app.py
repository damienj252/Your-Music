import flask as fl
import itertools as it

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