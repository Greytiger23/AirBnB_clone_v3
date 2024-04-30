#!/usr/bin/python3
""" int it file"""


from flask import Blueprint
from flask_cors import CORS
from api.v1.views.states import states_b
from api.v1.views.cities import cities_b

app_views = Blueprint('api_v1_views', __name__, url_prefix='/api/v1')
app_views.register_blueprint(states_b)
app_views.register_blueprint(cities_b)
CORS(app_views)

from .index import *

from api.v1.views import app_views
