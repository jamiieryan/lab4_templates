from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/name")
def nameonly():
	return "My name is Earl"
	
@app.route("/name/<name>", methods = ['GET'])
def name(name):
	name = request.args.get("name")
	return "Your Name is: " + name
	
@app.route("/firstname", methods = ['GET'])
def gettest():
	var = request.args.get("firstname")
	return "Hello " + var
	
@app.route("/lastname", methods = ['POST'])
def posttest():
#square brackets for POST var
	var = request.form["lastname"]
	return "Your Lastname is: " + var
	
#if(request.method == 'POST')
#else#

if __name__ == "__main__":
	app.run()
