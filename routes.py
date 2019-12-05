from flask import Blueprint, jsonify

from models import Men, db

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
