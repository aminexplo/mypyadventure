from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import FileField, StringField, SubmitField
from wtforms.validators import DataRequired


images = ('jpg', 'jpeg', 'png')


class AddForm(FlaskForm):
    label = StringField("Lable for the image", validators=[DataRequired()])
    file = FileField("Add new image", validators=[
                     FileRequired(), FileAllowed(images, "Only images are allowed...!")])
    submit = SubmitField("Add")


class PredictForm(FlaskForm):
    file = FileField("Send an image for label prediction", validators=[
                     FileRequired(), FileAllowed(images, "Only images are allowed...!")])
    submit = SubmitField("Predict")
