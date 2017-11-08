from flask import Flask, render_template, request, Response, send_file
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return '''
    	<html><body>
    	Welcome to possel.net! <a href="/getFile"> Click</a>
    	'''

@app.route("/resume")
def getFile():
	return send_file
	
