#!/usr/bin/pyhton3
"""new view for state objects that handle all the restful api"""


from flask import jsonify, request, abort, Blueprint
from models.state import State
from models.engine.db_storage import DBStorage


states_b = Blueprint('states', __name__)
storage = DBStorage()


@states_b.route('/states', methods=['GET'])
def get_states():
    """get the states"""
    states = []
    for state in storage.all(State).values():
        states.append(state.to_dict())
    return jsonify(states)


@states_b.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """get the state"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@states_b.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """delete state"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@states_b.route('/states', methods=['POST'])
def create_state():
    """create state"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Misssing name")
    state = State()
    state.name = request.get_json()['name']
    storage.new(state)
    storage.save()
    return jsonify(state.to_dict()), 201


@states_b.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """updates the state"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    storage.save()
    return jsonify(state.to_dict()), 200
