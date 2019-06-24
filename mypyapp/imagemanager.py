import os

import torch
from flask import current_app
from PIL import Image
from torchvision import models, transforms
from werkzeug.utils import secure_filename

from . import db
from .models import TrainingFile


class ImageManager:

    def __init__(self, file, label):
        self.file = file
        self.label = label

    def store_image(self):
        filename = secure_filename(self.file.filename)
        path = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
        self.file.save(path)
        tf = TrainingFile(filePath=path, label=self.label)
        db.session.add(tf)
        db.session.commit()
        return tf.id

    def predict(self):
        image = Image.open(self.file)
        transformed_image = transform(image)
        batch_t = torch.unsqueeze(transformed_image, 0)
        alexnet = models.alexnet(pretrained=True)
        alexnet.eval()
        out = alexnet(batch_t)
        with open(current_app.config["IMAGE_CLASSES_URI"]) as f:
            classes = [line.strip() for line in f.readlines()]
            _, indices = torch.sort(out, descending=True)
            percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
            [(classes[idx], percentage[idx].item()) for idx in indices[0][:5]]
        return classes[indices[0][0]]




transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )])
