#Originally adapted from:
# https://github.com/data-representation/example-project/blob/master/webapp.py

import flask as fl
import itertools as it

app = fl.Flask(__name__)

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/perms", methods=["GET", "POST"])
def perms():
	perms = [''.join(p) for p in it.permutations(fl.request.values["userinput"])]
	return '\n'.join(perms)

if __name__ == "__main__":
    app.run()