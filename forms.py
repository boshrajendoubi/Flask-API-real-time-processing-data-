from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import InputRequired

class FileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField('Charger')
 