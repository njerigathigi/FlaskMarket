from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class RegisterForm(FlaskForm):
    username = StringField(label="Username:", validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label="Email:", validators=[Email(), DataRequired()])
    password1 = PasswordField(label="Password:", validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label="Confirm Password:", validators=[EqualTo("password1"), DataRequired()])
    submit = SubmitField(label="Create Account")

#WTForms is a flexible forms validation and rendering library for Python web 
#development. It can work with whatever web framework and template engine you 
#choose. It supports data validation, CSRF protection, internationalization (I18N), 
#and more.
#Each field represents a data type and the field handles coercing form input to that datatype.
#In order to specify validation rules, fields contain a list of Validators.
# A validator simply takes an input, verifies it fulfills some criterion, such 
# as a maximum length for a string and returns. Or, if the validation fails, 
# raises a ValidationError.
