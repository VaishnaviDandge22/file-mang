from wtforms import PasswordField
from wtforms.validators import Regexp, EqualTo, ValidationError

class RegistrationForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Length(1,64),
                                    Email()])
    username = StringField('Username', validators=[
        DataRequired(),
        Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                   'Usernames must have only letters, numbers, dots, or underscores',
        )])
    password = PasswordField('Password', validators=[
        DataRequired(),
        EqualTo('password_confirm', message='Passwords do not match.'
        )])
    password_confirm = PasswordField('Password (confirm):',
                                     validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if Fan.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if Fan.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry! Username already in use.')
