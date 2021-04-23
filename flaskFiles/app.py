from flask import Flask
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('/flaskFiles/homepage.html')


@app.route('/about')
def about():
    return render_template('flaskFiles/about.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    error = None

    if request.methods == 'POST':

        if request.form['username'] != 'ethan' or request.form['password'] != password:
            error = "Incorrect input"
        else:
            return redirect(url_for('home'))

    return render_template('flaskFiles/login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
