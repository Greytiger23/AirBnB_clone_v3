#!/usr/bin/python3
""" int it file"""


from flask import Blueprint
from flask_cors import CORS
from api.v1.views.index import *
from api.v1.views.states import states_blueprint
from api.v1.views.cities import cities_blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
CORS(app_views)

app_views.register_blueprint(states_blueprint)
app_views.register_blueprint(cities_blueprint)
