from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thatsroughbuddy'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
                           InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[
                             InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember me')


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(
        message='Invalid email'), Length(max=50)])
    username = StringField('Username', validators=[
                           InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[
                             InputRequired(), Length(min=8, max=80)])


@app.route('/login', methods=['GET', 'POST'])
def login():

    navbar = "position:static;"
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('learningcontent'))

        return '<h1>Invalid username or password</h1>'
        # return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form, navbar=navbar)


@app.route('/signup', methods=['GET', 'POST'])
def signup():

    navbar = "position:static;"
    form = RegisterForm()

    if form.validate_on_submit():
        # using sha256 a message digests (assumed to be enough for this project)
        hashed_password = generate_password_hash(
            form.password.data, method='sha256')
        new_user = User(username=form.username.data,
                        email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        #  redirect after successful sign in to login page to login to new account
        return redirect(url_for('login'))
        # return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'
    return render_template('signup.html', form=form, navbar=navbar)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    # Return to homepage when logging out
    return redirect(url_for('home'))


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/about')
def about():

    navbar = "position:static;"
    return render_template('about.html', navbar=navbar)


@app.route('/learningcontent', methods=['GET', 'POST'])
def learningcontent():
    # If no user logged in currently in session, then redirect back to login
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    error = None
    return render_template('learningcontent.html', name=current_user.username)


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


@app.route('/Quiz', methods=['GET', 'POST'])
def Quiz():

    error = None
    return render_template('Quiz.html')


@app.route('/Self', methods=['GET', 'POST'])
def self():

    error = None
    return render_template('Self.html')

# @app.route('/Page1.html', methods=['GET', 'POST'])
# def learningcontent():

#     error = None
#     return render_template('Page1.html')

# @app.route('/Introduction.html', methods=['GET', 'POST'])
# def introduction():

#     error = None
#     return render_template('Introduction.html')

# @app.route('/Basics.html', methods=['GET', 'POST'])
# def basics():

#     error = None
#     return render_template('Basics.html')

# @app.route('/Rendering.html', methods=['GET', 'POST'])
# def rendering():

#     error = None
#     return render_template('Rendering.html')

# @app.route('/Components.html', methods=['GET', 'POST'])
# def components():

#     error = None
#     return render_template('Components.html')

# @app.route('/Handling.html', methods=['GET', 'POST'])
# def handling():

#     error = None
#     return render_template('Handling.html')

# @app.route('/Conditional.html', methods=['GET', 'POST'])
# def conditional():

#     error = None
#     return render_template('Conditional.html')

# @app.route('/Quiz.html', methods=['GET', 'POST'])
# def quiz():

#     error = None
#     return render_template('Quiz.html')

# @app.route('/Self.html', methods=['GET', 'POST'])
# def self():

#     error = None
#     return render_template('Self.html')


if __name__ == '__main__':
    app.run(debug=True)
