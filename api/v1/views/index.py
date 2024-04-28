#!/usr/bin/python3
""" index file"""


from flask import jsonify
from . import app_views
from models.engine.db_storage import DBStorage

storage = DBStorage()

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """displays the status"""
    stats = {}
    for obj_type in ['Amenity', 'City', 'Place', 'Review', 'State', 'Users']:
        stats[obj_type.lower()] = storage.count(classes[obj_type])
    return jsonify(stats)

# register the /stats route to the app_views object
app_views.add_url_rule('/stats', 'stats', stats)
