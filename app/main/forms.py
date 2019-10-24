from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, RadioField
from wtforms.validators import Reuired, Email, EqualTo
from wtforms import ValidationError

class PitchForm(FlaskForm):
    title = StringField('Title', validators = [Reuired()])
    description = TextAreaField("What would you like to pitch?", validators = [Required()])
    category = RadioField('Label', choices = [('promotionpitch', 'promotionpitch'), ('interviewpitch', 'interviewpitch'), ('pickuplines', 'pickuplines'), ('productpitch', 'productpitch')], validators = [Required()])
    submit - SubmitField('Submit')