from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Men(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def json(self):
        return {"id": self.id, "name": self.name}


class Request(db.Model):
    __tablename__ = 'request'
    item_id = db.Column(db.Integer, primary_key=True)
    reg_num = db.Column(db.String(120))
    create_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    update_date = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    request_type_item_id = db.Column(db.Integer, ForeignKey('requestType.item_id'))
    request_status_item_id = db.Column(db.Integer, ForeignKey('requestStatus.item_id'))
    person_item_id = db.Column(db.Integer, ForeignKey('person.item_id'))

    person = relationship('Person')
    requestType = relationship('RequestType')
    requestStatus = relationship('RequestStatus')

    def json(self):
        return {"item_id": self.item_id, "reg_num": self.reg_num, "person": self.person.json(), "requestType": self.requestType.json(), "requestStatus": self.requestStatus.json()}

class Person(db.Model):
    __tablename__ = 'person'
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    surname = db.Column(db.String(120))

    def json(self):
        return {"item_id": self.item_id, "name": self.name, "surname": self.surname}


class RequestType(db.Model):
    __tablename__ = 'requestType'
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def json(self):
        return {"item_id": self.item_id, "name": self.name}



class RequestStatus(db.Model):
    __tablename__ = 'requestStatus'
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def json(self):
        return {"item_id": self.item_id, "name": self.name}
