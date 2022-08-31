from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    content = TextAreaField('description', default='', validators=[DataRequired()])
    to_user_id = IntegerField('to_user_id', validators=[DataRequired()])