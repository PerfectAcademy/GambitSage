from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,PasswordField,RadioField,DateField, SelectField
from wtforms.validators import Email,DataRequired,EqualTo,Length




class ContactForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    email = StringField('Your Email', validators=[DataRequired(), Email()])
    phone=StringField('Your Phone Number', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])