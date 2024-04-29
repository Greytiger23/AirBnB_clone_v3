#!/usr/bin/python3
"""city api file"""


from flask import request, jsonify, abort
from models.city import City
from models.state import State
from models.engine.db_storage import DBStorage


def cities_resource(state_id=None):
    """handles all default restful api actions"""
    if state_id is not None:
        state = State.query.get(state_id)
        if state is None:
            abort(404)

    if request.method == 'GET':
        if state_id is not None:
            cities = City.query.filter_by(state_id=state_id).all()
            return jsonify([to_dict(city) for city in cities])
        else:
            city_id = request.views_args.get('city_id')
            city = City.query.get(city_id)
            if city is None:
                abort(404)
            return jsonify(to_dict(city))

    elif request.method == 'POST':
        if state_id is None:
            abort(404)
        name = request.json.get('name')
        if name is None:
            abort(400, description="Missing name")
        city = City(name=name, state_id=state_id)
        city.save()
        return jsonify(to_dict(city)), 201

    elif request.method == 'POST':
        city_id = request.view_args.get('city_id')
        city = City.query.get(city_id)
        if city is None:
            abort(404)
        new_data = request.get_json()
        if new_data is None:
            abort(400, description="Not a JSON")
        for key, value in new_data.items():
            if key not in ['id', 'state_id', 'created_id', 'updated_at']:
                setattr(city, key, value)
        city.save()
        return jsonify(to_dict(city))

    elif request.method == 'DELETE':
        city_id = request.view_args.get('city_id')
        city = City.query.get(city_id)
        if city is None:
            abort(404)
        city.delete()
        return jsonify({}), 200
