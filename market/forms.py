from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError #classes
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user: #if user != None
            raise ValidationError("Username already exists! Please try a different username") #built-in exception class
    
    def validate_email_address(self, email_to_check):
        email_address = User.query.filter_by(email_address=email_to_check.data).first()
        if email_address:
            raise ValidationError("Email Address already exists!Please try a diffent email address.")
    
    username = StringField(label="Username:", validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label="Email:", validators=[Email(), DataRequired()]) #you must install email_validator for email validation(pip install email_validator)
    password1 = PasswordField(label="Password:", validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label="Confirm Password:", validators=[EqualTo("password1"), DataRequired()])
    submit = SubmitField(label="Create Account")

class LoginForm(FlaskForm):
    username = StringField(label="Username:", validations=[DataRequired()])
    password = PasswordField(label="Password:", validations=[DataRequired()])
    submit = SubmitField(label="Sign In")

#WTForms is a flexible forms validation and rendering library for Python web 
#development. It can work with whatever web framework and template engine you 
#choose. It supports data validation, CSRF protection, internationalization (I18N), 
#and more.
#Each field represents a data type and the field handles coercing form input to that datatype.
#In order to specify validation rules, fields contain a list of Validators.
#A validator simply takes an input, verifies it fulfills some criterion, such 
#as a maximum length for a string and returns. Or, if the validation fails, 
#raises a ValidationError.

#custom validators
# we are allowed to create our own validators by the wtforms-validators library.
# They must begin with the prefix 'validate_'(validate underscore) followed by a field defined
# in the form class.
# FlaskForm searches for these and executes the code.
