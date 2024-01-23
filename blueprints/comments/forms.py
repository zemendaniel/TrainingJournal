from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, length


class CreateCommentForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), length(1, 32)])
    content = TextAreaField('content', validators=[DataRequired(), length(1, -1)])
    submit = SubmitField('Create')
