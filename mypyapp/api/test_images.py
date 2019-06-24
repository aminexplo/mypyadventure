import json
import os
from io import BytesIO

import pytest
from PIL import Image

from mypyapp import create_app


@pytest.fixture
def app():
    app = create_app('test')
    with app.app_context():
        yield app


@pytest.fixture
def client(app):
    yield app.test_client()


@pytest.fixture
def temp_image_file():
    file = BytesIO()
    image = Image.new('RGBA', size=(512, 512), color=(155, 0, 0))
    image.save(file, 'png')
    file.name = 'test.png'
    file.seek(0)
    return file

@pytest.fixture
def dog_image_file():
    file = BytesIO()
    image = Image.open(os.path.join(os.getcwd(), 'mypyapp', 'api', 'test_dog.png'))
    image.save(file, 'png')
    file.name = 'test_dog.png'
    file.seek(0)
    return file

def test_images_store_image_with_label(client, temp_image_file):
    r = client.post(
        '/api/images/add',
        data={'image': temp_image_file},
        headers={'label': 'test_label'},
        follow_redirects=True
    )
    assert r.status_code == 201


def test_images_predict_label(client, dog_image_file):
    r = client.post(
        '/api/images/predict',
        data={'image': dog_image_file},
        follow_redirects=True
    ) 
    jsonResp = json.loads(r.data)
    assert r.status_code == 200
    assert jsonResp['label'] == 'Siberian husky'
