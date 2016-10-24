from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def hell():
	return "Hello World!"

@app.route("/hello/")
@app.route("/hello/<name>", methods = ['GET'])
def hello(name=None):
	name = request.args.get("name")
	return render_template("hello.html", name=name)

#@app.route("/name")
#def nameonly():
#	return "My name is Earl"
	
#@app.route("/name/<name>", methods = ['GET'])
#def name(name):
#	name = request.args.get("name")
#	return "Your Name is: " + name
#	
#@app.route("/firstname", methods = ['GET'])
#def gettest():
#	var = request.args.get("firstname")
#	return "Hello " + var
	
#@app.route("/lastname", methods = ['POST'])
#def posttest():
#square brackets for POST var
#	var = request.form["lastname"]
#	return "Your Lastname is: " + var
	
	




if __name__ == "__main__":
	app.run()
	
	

