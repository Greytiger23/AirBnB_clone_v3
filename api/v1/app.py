#!/usr/bin/python3
"""create file appp"""


import os
from flask import Flask, jsonify
from api.v1.views import app_views
from api.v1.views.states import states
from api.v1.views.cities import cities
from models import storage


app = Flask(__name__)
app.register_blueprint(app_views)
app.register_blueprint(states)
app.register_blueprint(cities)


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
