#!/usr/bin/python3
"""create a new view for amenity"""


from flask import jsonify, request, abort
from models.amenity import Amenity
from models import storage
from api.v1.views import app_views


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    """retrieves the list of all amentiy"""
    amenities = storage.all(Amenity).values()
    return jsonify([amenity.to_dict() for amenity in amenities])


@app_views.route(
        '/amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def get_amenity(amenity_id):
    """retrieves a amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route(
        '/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_amenity(amenity_id):
    """deletes a amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_amenity():
    """creates a amenity"""
    if not request.get_json():
        abort(400, "Not a JSON")
    data = request.get_json()
    if 'name' not in data:
        abort(400, "Missing name")
    amenity = Amenity(**data)
    storage.new(amenity)
    storage.save()
    return jsonify(amenity.to_dict()), 201


@app_views.route(
        '/amenities/<amenity_id>', methods=['PUT'], strict_slashes=False)
def update_amenity(amenity_id):
    """updates a amenity"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)
    storage.save()
    return jsonify(amenity.to_dict()), 200
