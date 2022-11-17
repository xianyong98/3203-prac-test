from flask import Flask, render_template, redirect, request, url_for
import re

app = Flask(__name__)


@app.route('/')
def home():
	return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
	data = request.form.get('login')
	#flag = method(data)
	with open("10-million-password-list-top-1000.txt") as f: common_values = [line.rstrip("\n") for line in f]
	if any(value == data for value in common_values):
		return render_template('index.html')
	if data=='':
		return render_template('index.html')
	else:
		return render_template('login.html', login=data)
	
	
if __name__ == '__main__':
	app.run()
