from flask import Flask, render_template, url_for, flash, redirect
from datetime import date
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '9c71ebe7efdf0fd53059fdc3f7bdddfa'

posts = [
    {
        'author': 'I K',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': date.today()
    },
    {
        'author': 'M K',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': date.today()
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'idah@blog.com' and form.password.data == '1':
            flash('You are logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful.Check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
