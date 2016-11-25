# Author: Damien Joyce
# Date: 

# Originally adapted from: https://github.com/data-representation/example-project/blob/master/webapp.py

import flask as fl

import itertools as it

app = fl.Flask(__name__)

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/perms", methods=["GET", "POST"])
def perms():
	perms = [''.join(p) for p in it.permutations(fl.request.values["artistinput"])]
	return '\n'.join(perms)
#-------------------------------------------------------------------------------------------------------------------------------
class couchdb.client.Server(url='http://localhost:5984/', full_commit=True, session=None)
server = Server() # connects to the local_server
remote_server = Server('http://example.com:5984/')
secure_remote_server = Server('https://username:password@example.com:5984/')

db = server.create('music')
db.name
#-------------------------------------------------------------------------------------------------------------------------------
class couchdb.client.Database(url, name=None, session=None)
server = Server()
db = server.create('music')

doc_id, doc_rev = db.save({'artist': 'Chris Malinchak', 'song': 'Wonderful'})

doc = db[doc_id]
doc

doc.id, doc.rev

doc['artist']
doc['song']

doc['artist'] = artistinput
doc['song'] = songinput


if __name__ == "__main__":
    app.run()
    
