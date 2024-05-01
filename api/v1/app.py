#!/usr/bin/python3
"""create file appp"""


import os
from flask import Flask, jsonify
from api.v1.views import app_views
from api.v1.views.states import states as states_b
from api.v1.views.cities import cities as cities_b
from api.v1.views.amenities import amenities_b
from api.v1.views.users import users_b
from api.v1.views.places import places_b
from api.v1.views.places_reviews import reviews_b
from models import storage


app = Flask(__name__)
app.register_blueprint(app_views)
app.register_blueprint(states_b)
app.register_blueprint(cities_b)
app.register_blueprint(amenities_b)
app.register_blueprint(users_b)
app.register_blueprint(places_b)
app.register_blueprint(reviews_b)


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
