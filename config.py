import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "easy-to-guess"
    UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER") or os.path.join(
        basedir, "uploads", "images")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'mypyadv.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    IMAGE_CLASSES_URI = os.environ.get('IMAGE_CLASSES_URI') or os.path.join(
        basedir, "image_classes.txt")

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
