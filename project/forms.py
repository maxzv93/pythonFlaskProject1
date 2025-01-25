from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Email, Length, InputRequired


class MessageForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired(), Length(5, 32)])
    email = StringField("Email: ", validators=[Email()])
    message = TextAreaField("Message", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[Length(9, 24), InputRequired()])
    submit = SubmitField("Submit")
