from . import db


class TrainingFile(db.Model):

    __tablename__ = "training_file"

    id = db.Column(db.Integer, primary_key=True)
    filePath = db.Column(db.String(512))
    label = db.Column(db.String(128))

    def __repr__(self):
        return '<TrainingFile {}>'.format(self.filePath)
