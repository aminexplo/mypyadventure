from flask import Blueprint

bp = Blueprint('api', __name__)

from mypyapp.api import images, errors
