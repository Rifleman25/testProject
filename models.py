from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Men(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def json(self):
        return {"id": self.id, "name": self.name}


class Request(db.Model):
    itemId = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer)
    regNum = db.Column(db.String(120))
    regDate = db.Column(db.Date)
