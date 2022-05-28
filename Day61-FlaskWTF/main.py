from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "iwucuwebcuibwiuvbwuebviuwebvi"
Bootstrap(app)


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(8)])
    submit = SubmitField(label='Log In')


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
