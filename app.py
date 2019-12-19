import datetime

from flask import Flask

from models import db, Men, Person, Request, RequestType, RequestStatus
from routes import api, index

app = Flask(__name__)
app.register_blueprint(index)
app.register_blueprint(api)
db.init_app(app)
with app.app_context():
    db.create_all()

    #Типы заявок
    provision_tsr = RequestType(name="Обеспечение ТСР")
    compensation_tsr = RequestType(name="Компенсация ТСР")
    rehab = RequestType(name="Ранняя реабилитация")
    db.session.add(provision_tsr)
    db.session.add(compensation_tsr)
    db.session.add(rehab)

    #Статусы завок
    draft = RequestStatus(name="Черновик")
    consideration = RequestStatus(name="Рассмотрение")
    suspended = RequestStatus(name="Приостановлена")
    closed = RequestStatus(name="Звкрыта")
    completed = RequestStatus(name="Обеспечение закончено")
    db.session.add(draft)
    db.session.add(consideration)
    db.session.add(suspended)
    db.session.add(closed)
    db.session.add(completed)

    #Получатели услуг
    anton = Person(name='Anton', surname='Istomin')
    stas = Person(name='Станислав', surname='Тифакин')
    sergey = Person(name='Сергей', surname='Иванов')

    db.session.add(anton)
    db.session.add(stas)
    db.session.add(sergey)
    db.session.commit()

    #Заявки
    antonCompensation = Request(reg_num='1', person_item_id=anton.item_id, request_type_item_id=compensation_tsr.item_id, request_status_item_id=draft.item_id)
    antonRehab = Request(reg_num='35', person_item_id=anton.item_id, request_type_item_id=rehab.item_id, request_status_item_id=closed.item_id)
    stasprovision = Request(reg_num='1514', person_item_id=stas.item_id, request_type_item_id=provision_tsr.item_id, request_status_item_id=consideration.item_id)
    antonCompensation = Request(reg_num='1', person_item_id=sergey.item_id, request_type_item_id=compensation_tsr.item_id, request_status_item_id=completed.item_id)
    db.session.add(antonCompensation)
    db.session.add(antonRehab)
    db.session.add(stasprovision)
    db.session.add(antonCompensation)
    db.session.commit()

if __name__ == '__main__':
    app.run()
