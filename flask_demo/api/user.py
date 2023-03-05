from flask import jsonify, request
from flask.blueprints import Blueprint
from flask_demo.database import db, User

user = Blueprint('user', __name__)


@user.get('<string:id>')
def get_user(id):
    print(id)
    u = User.query.filter(User.id == id).first()
    if u is None:
        return jsonify({
            'code': 404
        })
    return jsonify({
        'code': 200,
        'data': {
            'user': u.to_json()
        }
    })


@user.post('')
def create_user():
    data = request.json

    if len(User.query.filter(User.id == data['id']).all()) > 0:
        return jsonify({
            'code': 500
        })
    u = User(
        id=data['id'],
        username=data['username'],
        password=data['password']
    )
    print(u)
    db.session.add(u)
    db.session.commit()

    return jsonify({
        'code': 200,
        'data': {
            'user': u.to_json()
        }
    })


@user.post('<string:id>/username/<string:username>')
def set_username(id, username):
    u = User.query.filter(User.id == id).first()
    if u is None:
        return jsonify({
            'code': 404
        })
    u.username = username
    db.session.commit()
    return jsonify({
        'code': 200,
        'data': {
            'user': u.to_json()
        }
    })


@user.delete('<string:id>')
def delete_user(id):
    print(id)
    u = User.query.filter(User.id == id).first()
    if u is None:
        return jsonify({
            'code': 404
        })
    db.session.delete(u)
    db.session.commit()

    return jsonify({
        'code': 200,
        'data': {
            'user': u.to_json()
        }
    })
