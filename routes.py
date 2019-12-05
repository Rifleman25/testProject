from flask import Blueprint, jsonify

from models import Men, db, Request, Person, RequestType

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

@index.route('/persons/add/name/<string:person_name>/surname/<string:person_surname>')
def addPerson(person_name, person_surname):
    newPerson = Person(name=person_name, surname=person_surname)
    db.session.add(newPerson)
    db.session.commit()
    return 'Ok'

@index.route('/reqiestType/add/name/<string:name>')
def addRequestType(name):
    newRequestType = RequestType(name=name)
    db.session.add(newRequestType)
    db.session.commit()
    return 'Ok'

@index.route('/')
@index.route('/index')
def get_index():
    return '''
            <html>
                <title>
                        Супер крутой веб-сервис
                </title>
                <body>
                    <a href="/api/mens">Mens</a>
                </body
            </html
        '''
