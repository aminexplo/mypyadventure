import json

from flask import jsonify, request, url_for

from mypyapp import db
from mypyapp.imagemanager import ImageManager
from mypyapp.models import TrainingFile

from . import bp
from .errors import bad_request


@bp.route('/images/add/', methods=['GET', 'POST'])
def store_image_with_label():
    if 'image' not in request.files or 'label' not in request.headers:
        return bad_request('An image and a lable are required...!')
    file = request.files['image']
    label = request.headers['label']
    im = ImageManager(file,label)
    result = im.store_image()
    if result:
        response = jsonify({'id':result})
        response.status_code = 201
        return response
    else:
        return bad_request('Could not upload the image...!')

@bp.route('/images/predict/', methods=['GET', 'POST'])
def predict_label():
    if 'image' not in request.files:
        return bad_request('An image is required...!')
    file = request.files['image']
    im = ImageManager(file,'')
    result = im.predict()
    if result:
        response = jsonify({'label' : result})
        response.status_code = 200
        return response
    else:
        return bad_request('Could not predict...!')
