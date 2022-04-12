from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class CommentForm(FlaskForm):
    text = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Add Comment')