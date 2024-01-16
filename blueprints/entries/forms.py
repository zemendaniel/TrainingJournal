from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, length


class CreateEntryForm(FlaskForm):
    description = TextAreaField('Description', validators=[DataRequired(), length(1, -1)])
    submit = SubmitField('Create')


class EditEntryForm(FlaskForm):
    description = TextAreaField('Description', validators=[DataRequired(), length(1, -1)])
    submit = SubmitField('Save')