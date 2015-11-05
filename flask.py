from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def main():
	return render_template("main.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/ad')
def ad():
	return render_template("ad.html")

@app.route('/gallery')
def gallery():
	return render_template("gallery.html")

@app.route('/help')
def help():
	return render_template("help.html")

@app.route('/log_in')
def log_in():
	return render_template("log_in")

@app.route('/sign_up')
def sign_up():
	return render_template('sign_up.html')


#@app.route('/welcome/', methods =['POST'])
#@app.route('/welcome/<firstname>')
#def welcome():
#	a = request.form['firstname']
#	return render_template('welcome.html', name = a)

if __name__=="__main__":
	app.run()
