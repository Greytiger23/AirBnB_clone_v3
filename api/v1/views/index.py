#!/usr/bin/python3
""" index file"""


from flask import jsonify
from models import storage
from models.engine.db_storage import classes
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """displays the status"""
    return jsonify({"status": "OK"})

# register the /status route thr app_view object
app_views.add_url_rule('/status', 'status', status)


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """displays the status"""
    stats = {}
    for obj_type in ['Amenity', 'City', 'Place', 'Review', 'State', 'User']:
        stats[obj_type.lower()] = storage.count(classes[obj_type])
    return jsonify(stats)

# register the /stats route to the app_views object
app_views.add_url_rule('/stats', 'stats', get_stats)
