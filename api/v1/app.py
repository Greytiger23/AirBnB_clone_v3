#!/usr/bin/python3
"""create file appp"""


from flask import Flask, jsonify
from flask_cors import CORS
import os
from api.v1.views import app_views
from models import storage


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


app.register_blueprint(app_views)


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
