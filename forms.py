from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddSearchForm(FlaskForm):
    searchinput = StringField("SEARCH", validators=[DataRequired()])