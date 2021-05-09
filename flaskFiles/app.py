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

        if request.form['username'] != 'testpassword' or request.form['password'] != password:
            error = "Incorrect input"
        else:
            return redirect(url_for('home'))

    return render_template('login.html', error=error)


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/Page1', methods=['GET', 'POST'])
def learningcontent():

    error = None
    return render_template('Page1.html')


@app.route('/Introduction', methods=['GET', 'POST'])
def introduction():

    error = None
    return render_template('Introduction.html')


@app.route('/Basics', methods=['GET', 'POST'])
def basics():

    error = None
    return render_template('Basics.html')


@app.route('/Rendering', methods=['GET', 'POST'])
def rendering():

    error = None
    return render_template('Rendering.html')


@app.route('/Components', methods=['GET', 'POST'])
def components():

    error = None
    return render_template('Components.html')


@app.route('/Handling', methods=['GET', 'POST'])
def handling():

    error = None
    return render_template('Handling.html')


@app.route('/Conditional', methods=['GET', 'POST'])
def conditional():

    error = None
    return render_template('Conditional.html')


@app.route('/EndOfTutorial', methods=['GET', 'POST'])
def EndOfTutorial():

    error = None
    return render_template('EndOfTutorial.html')


@app.route('/Quiz1', methods=['GET', 'POST'])
def Quiz1():

    error = None
    return render_template('Quiz1.html')


@app.route('/Quiz2', methods=['GET', 'POST'])
def Quiz2():

    error = None
    return render_template('Quiz2.html')


@app.route('/Quiz3', methods=['GET', 'POST'])
def Quiz3():

    error = None
    return render_template('Quiz3.html')


@app.route('/Self', methods=['GET', 'POST'])
def self():

    error = None
    return render_template('Self.html')


if __name__ == '__main__':
    app.run(debug=True)
