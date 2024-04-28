#!/usr/bin/python3
""" index file"""


from flask import jsonify
from . import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """displays the status"""
    return jsonify({'status': 'OK'})

# register the /status route to the app_views object
app_views.add_url_rule('/status', 'status', status)
