from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static/')

@app.route('/')
def home():
	return render_template("index.html")	

@app.route('/about/')
def about():
	return render_template("about.html")

@app.route('/program/')
def program():
	return render_template("program.html")

@app.route('/contact/')
def contact():
	return render_template("contact.html")

if __name__ == "__main__":
	app.run(debug=True)
