#!/usr/bin/python3
"""creates new views for place reviews"""


from flask import jsonify, request, abort
from models.place import Place
from models.review import Review
from models.user import User
from models import storage
from api.v1.views import app_views


@app_views.route('/places/<place_id>/reviews', methods=['GET'], strict_slashes=False)
def get_reviews(place_id):
    """retrieves the list of all review"""
    place = storage.get('Place', place_id)
    if place is None:
        abort(404)
    reviews = storage.all('Review').values()
    filtered_reviews = [review for review in reviews if review.place_id == place_id]
    return jsonify(filtered_reviews)


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_review(review_id):
    """retrieves a review"""
    review = storage.get('Review', review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'], strict_slashes=False)
def delete_review(review_id):
    """deletes a review"""
    review = storage.get('Review', review_id)
    if review is None:
        abort(404)
    review.delete()
    return jsonify({}), 200


@app_views.route('/places/<place_id>/reviews', methods=['POST'], strict_slashes=False)
def create_review(place_id):
    """creates a review"""
    place = storage.get('Place', place_id)
    if place is None:
        abort(404)
    if not request.get_json():
        abort(400, description='Not a JSON')
    data = request.get_json()
    if 'user_id' not in data:
        abort(400, description='Missing user_id')
    user = storage.get('User', data['user_id'])
    if user is None:
        abort(404)
    if 'text' not in data:
        abort(400, descripton='Missing text')
    new_review = storage.create('Review', **data)
    return jsonify(new_review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    """updates a review"""
    review = storage.get('Review', review_id)
    if review is None:
        abort(404)
    if not request.get_json():
        abort(400, description='Not a JSON')
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'user_id', 'place_id', 'created_at',
                       'updated_at']:
            setattr(review, key, value)
    review.save()
    return jsonify(review.to_dict()), 200
