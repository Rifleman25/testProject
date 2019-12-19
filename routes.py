from flask import Blueprint, jsonify

from models import Men, db, Request, Person, RequestType, RequestStatus

index = Blueprint('index', __name__, url_prefix='/')
api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/mens')
def hello():
    return jsonify([(lambda men: men.json())(men) for men in Men.query.all()])


@api.route('/men/id/<int:men_id>')
def get_men(men_id):
    men = Men.query.get(men_id)
    return jsonify(men.json()) if men else ''


@api.route('/men/name/<string:men_name>')
def set_men(men_name):
    db.session.add(Men(name=men_name))
    db.session.commit()
    return 'done'

@index.route('/requests')
def getRequesits():
    return jsonify([(lambda request: request.json())(request) for request in Request.query.all()])

@index.route('/persons')
def getPersons():
    return jsonify([(lambda person: person.json())(person) for person in Person.query.all()])

@index.route('/request_types')
def getRequestTypes():
    return jsonify([(lambda type: type.json())(type) for type in RequestType.query.all()])

@index.route('/request_statuses')
def getRequestStatuses():
    return jsonify([(lambda status: status.json())(status) for status in RequestStatus.query.all()])

@index.route('/persons/add/reg_num/<string:reg_num>/typeId/<int:typeId>/statusId/<int:statusId>/personId/<int:personId>')
def addRequest(reg_num, typeId, statusId, personId):
    newrequest = Request(reg_num=reg_num, request_type_item_id=typeId, request_status_item_id=statusId, person_item_id = personId)
    db.session.add(newrequest)
    db.session.commit()
    return 'Ok'

@index.route('/persons/add/name/<string:person_name>/surname/<string:person_surname>')
def addPerson(person_name, person_surname):
    newPerson = Person(name=person_name, surname=person_surname)
    db.session.add(newPerson)
    db.session.commit()
    return 'Ok'

@index.route('/persons/update/itemId/<int:itemId>/name/<string:person_name>')
def updatePersonName(itemId, person_name):
    person = Person.query.get(itemId)
    person.person_name = person_name
    db.session.add(person)
    db.session.commit()
    return 'Ok'

@index.route('/persons/update/itemId/<int:itemId>/surname/<string:person_surname>')
def updatePersonSurname(itemId, person_surname):
    person = Person.query.get(itemId)
    person.person_surname = person_surname
    db.session.add(person)
    db.session.commit()
    return 'Ok'

@index.route('/requestType/add/name/<string:name>')
def addRequestType(name):
    newRequestType = RequestType(name=name)
    db.session.add(newRequestType)
    db.session.commit()
    return 'Ok'

@index.route('/requestType/update/itemId/<int:itemId>/name/<string:name>')
def updateRequestType(itemId, name):
    requestType = RequestType.query.get(itemId)
    requestType.name = name
    db.session.add(requestType)
    db.session.commit()
    return 'Ok'

@index.route('/requestStatus/add/name/<string:name>')
def addRequestStatus(name):
    newRequestStatus = RequestStatus(name=name)
    db.session.add(newRequestStatus)
    db.session.commit()
    return 'Ok'

@index.route('/requestStatus/update/itemId/<int:itemId>/name/<string:name>')
def updateRequestStatus(itemId, name):
    requestStatus = RequestStatus.query.get(itemId)
    requestStatus.name = name
    db.session.add(requestStatus)
    db.session.commit()
    return 'Ok'

@index.route('/')
@index.route('/index')
def get_index():
    return '''
            <html>
                <title>
                        Сервис заявок
                </title>
                <body>
                    <a href="/requests">Заявки</a>
                    <a href="/persons">Получатели услуг</a>
                    <a href="/request_statuses">Статусы заявок</a>
                    <a href="/request_types">Типы заявок</a>
                </body
            </html
        '''
