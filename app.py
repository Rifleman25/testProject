from flask import Flask

from models import db, Men, Person, Request, RequestType
from routes import api, index

app = Flask(__name__)
app.register_blueprint(index)
app.register_blueprint(api)
db.init_app(app)
with app.app_context():
    db.create_all()
    person = Person(name='Anton', surname='Istomin')
    provision_tsr = RequestType(name="Обеспечение ТСР")
    compensation_tsr = RequestType(name="Компенсация ТСР")
    rehab = RequestType(name="Ранняя реабилитация")
    db.session.add(provision_tsr)
    db.session.add(compensation_tsr)
    db.session.add(rehab)
    db.session.add(person)
    db.session.commit()
    request = Request(reg_num='1', person_item_id=person.item_id, request_type_item_id=compensation_tsr.item_id)
    db.session.add(request)
    db.session.commit()

if __name__ == '__main__':
    app.run()
