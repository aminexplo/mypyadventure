import os
from datetime import datetime

from flask import (Blueprint, current_app, flash, redirect, render_template,
                   request)
from werkzeug.utils import secure_filename

from . import db
from .forms import AddForm, PredictForm
from .imagemanager import ImageManager
from .models import TrainingFile

bp = Blueprint('main', __name__)


@bp.route("/")
def about():
    return render_template("about.html")


@bp.route("/add/", methods=["GET", "POST"])
def add():
    form = AddForm()
    if request.method == "POST" and form.validate_on_submit():
        f = form.file.data
        im = ImageManager(f, form.label.data)
        if im.store_image():
            flash("File uploaded successfully...!")
        else:
            flash("Error in uploading the file...!")
        return redirect(request.url)

    return render_template("add.html", form=form)


@bp.route("/predict/", methods=["GET", "POST"])
def predict():
    form = PredictForm()
    if request.method == "POST" and form.validate_on_submit():
        f = form.file.data
        im = ImageManager(f, "")
        img_label = im.predict()
        return render_template("predict.html", form=form, img_label=img_label)
    return render_template("predict.html", form=form, img_label="")


@bp.context_processor
def inject_now():
    return {"now": datetime.utcnow()}
