# Import Form and RecaptchaField (optional)
from flask.ext.wtf import Form # , RecaptchaField
from wtforms import StringField, BooleanField
# Import Form validators
from wtforms.validators import DataRequired


# Define the login form (WTForms)

class LoginForm(Form):
	openid = StringField('openid', validators=[DataRequired()])
	remember_me = BooleanField('remember_me', default=False)
    # email    = TextField('Email Address', [Email(),
    #             Required(message='Forgot your email address?')])
    # password = PasswordField('Password', [
    #             Required(message='Must provide a password. ;-)')])
