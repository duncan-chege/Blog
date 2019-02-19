from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField, ValidationError
from wtforms.validators import Required,Email,EqualTo
from ..models import Writer

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    name = StringField('Your Name ',validators=[Required()])
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    submit = SubmitField('Create an Account')

    def validate_email(self,data_field):
            if Writer.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')
