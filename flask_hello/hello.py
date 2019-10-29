from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
	title = "hello"
	message = "hello flask"
	#render index.html
	return render_template('index.html', message = message, title = title)

@app.route("/post", methods = ['GET', 'POST'])
def post():
	title = "post page"
	if request.method == 'POST':
		name = request.form['name']
		return render_template('index.html', name = name, title = title)
	else:
		return redirect(url_for('index'))

if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0',port=8080)
