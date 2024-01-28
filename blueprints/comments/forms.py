from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, TextAreaField, SubmitField, HiddenField
from wtforms.validators import DataRequired, length


class CreateCommentForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(1, 32)])
    content = TextAreaField('Content', validators=[DataRequired(), length(1, -1)])
    submit = SubmitField('Create')
