#!/usr/bin/python3
"""create a new voew for user"""


from flask import jsonify, request, abort, Blueprint
from models import storage
from api.v1.views import app_views


users_b = Blueprint('users', __name__)


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """retrieves the list of all users"""
    users = storage.all('User').values()
    return jsonify([user.to_dict() for user in users])


@app_views.route(
        '/users/<string:user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """retrieves a user object"""
    user = storage.get('User', user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """creates a user"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    if 'email' not in data:
        abort(400, description="Missing email")
    if 'password' not in data:
        abort(400, description="Missing password")
    new_user = storage.create('User', **data)
    return jsonify(new_user.to_dict()), 201


@app_views.route(
        '/users/<string:user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """updates a user"""
    user = storage.get('User', user_id)
    if user is None:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict()), 200


@app_views.route(
        '/users/<string:user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """deletes a user object"""
    user = storage.get('User', user_id)
    if user is None:
        abort(404)
    user.delete()
    return jsonify({}), 200
