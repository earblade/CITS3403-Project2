from flask import Flask
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    error = None

    if request.method == 'POST':

        if request.form['username'] != 'ethan' or request.form['password'] != password:
            error = "Incorrect input"
        else:
            return redirect(url_for('home'))

    return render_template('login.html', error=error)

@app.route('/Page1.html', methods=['GET', 'POST'])
def learningcontent():

    error = None
    return render_template('Page1.html')

@app.route('/Introduction.html', methods=['GET', 'POST'])
def introduction():

    error = None
    return render_template('Introduction.html')

@app.route('/Basics.html', methods=['GET', 'POST'])
def basics():

    error = None
    return render_template('Basics.html')

@app.route('/Rendering.html', methods=['GET', 'POST'])
def rendering():

    error = None
    return render_template('Rendering.html')

@app.route('/Components.html', methods=['GET', 'POST'])
def components():

    error = None
    return render_template('Components.html')

@app.route('/Handling.html', methods=['GET', 'POST'])
def handling():

    error = None
    return render_template('Handling.html')

@app.route('/Conditional.html', methods=['GET', 'POST'])
def conditional():

    error = None
    return render_template('Conditional.html')

@app.route('/Quiz.html', methods=['GET', 'POST'])
def quiz():

    error = None
    return render_template('Quiz.html')

@app.route('/Self.html', methods=['GET', 'POST'])
def self():

    error = None
    return render_template('Self.html')


if __name__ == '__main__':
    app.run(debug=True)
