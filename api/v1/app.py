#!/usr/bin/python3
"""create file appp"""


import os
from flask import Flask, jsonify
from api.v1 import app
from models import storage


@app.teardown_appcontext
def teardown_appcontext(exception):
    """declare a method to handle"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """return error page"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
