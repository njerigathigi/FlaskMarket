from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label="username")
    email_address = StringField(label="email")
    password1 = PasswordField(label="password1")
    password2 = PasswordField(label="password2")
    submit = SubmitField(label="submit")



#WTForms is a flexible forms validation and rendering library for Python web 
#development. It can work with whatever web framework and template engine you 
#choose. It supports data validation, CSRF protection, internationalization (I18N), 
#and more.
#Each field represents a data type and the field handles coercing form input to that datatype.
#In order to specify validation rules, fields contain a list of Validators.
# A validator simply takes an input, verifies it fulfills some criterion, such 
# as a maximum length for a string and returns. Or, if the validation fails, 
# raises a ValidationError.
