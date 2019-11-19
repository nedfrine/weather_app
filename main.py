from flask import Flask, flash, redirect, render_template, request, session, abort
import requests
app = Flask(__name__,static_folder="static")

@app.route("/city/<name>")
def details(name):
	api_key = '7c923a9b52a44023a20bf4d7b0330459'
	url = 'http://api.openweathermap.org/data/2.5/weather?appid=7c923a9b52a44023a20bf4d7b0330459&units=metric&q='+ name
	r = requests.get(url)
	data = r.text
	return data
	
@app.route("/")
def render():
	return render_template('rotate.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)