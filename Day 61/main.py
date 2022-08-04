from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,validators
from wtforms.validators import DataRequired, Email, EqualTo, length, Length
import email_validator
from flask_bootstrap import Bootstrap

class MyForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message=u"Invalid Email, stoopid?")])
    password = PasswordField('Password', validators=[Length(min=8), DataRequired()])
    submit = SubmitField(label="Login")


app = Flask(__name__)
app.secret_key = 'secret'
Bootstrap(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)

