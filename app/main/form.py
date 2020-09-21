from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators = [Required()])
    submit = SubmitField('Save')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[Required()])
    submit = SubmitField('Comment')

class PitchForm(FlaskForm):
    category = SelectField('Category :', choices=[('Tech','Tech'),('Job','Job'),('Environment','Environment')],validators=[Required()])
    title = StringField('Title :', validators=[Required()])
    post = TextAreaField('Your Pitch :', validators=[Required()])
    submit = SubmitField('Pitch')