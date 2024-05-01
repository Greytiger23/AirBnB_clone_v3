#!/usr/bin/python3
"""create neww view for place"""


from flask import jsonify, request, abort
from models.city import City
from models.place import Place
from models.user import User
from models import storage
from api.v1.views import app_views


@app_views.route(
    '/cities/<string:city_id>/places', methods=['GET'], strict_slashes=False)
def get_places(city_id):
    """retrieves the list of all places"""
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    places = storage.all('Place').values()
    filtered_places = [place for place in places if place.city_id == city_id]
    return jsonify(filtered_places)


@app_views.route(
        '/places/<string:place_id>', methods=['GET'], strict_slashes=False)
def get_place(place_id):
    """retrieves a place object"""
    place = storage.get('Place', place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route(
    '/cities/<string:city_id>/places', methods=['POST'], strict_slashes=False)
def create_place(city_id):
    """creates a place"""
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    if not request.get_json():
        abort(400, description='Not a JSON')
    data = request.get_json()
    if 'user_id' not in data:
        abort(400, description='Missing user_id')
    user = storage.get('User', data['user_id'])
    if user is None:
        abort(404)
    if 'name' not in data:
        abort(400, description='Missing name')
    new_place = storage.create('Place', **data)
    return jsonify(new_place.to_dict()), 201

@app_views.route(
        '/places/<string:place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    """updates a place"""
    place = storage.get('Place', place_id)
    if place is None:
        abort(404)
    if not request.get_json():
        abort(400, description='Not a JSON')
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'user_id', 'city_id', 'created_at', 'updated_at']:
            setattr(place, key, value)
    place.save()
    return jsonify(place.to_dict()), 200

@app_views.route(
        '/places/<string:place_id>', methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    """deletes a place"""
    place = storage.get('Place', place_id)
    if place is None:
        abort(404)
    place.delete()
    return jsonify({}), 200
