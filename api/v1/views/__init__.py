#!/usr/bin/python3
""" int it file"""


from flask import Blueprint
from flask_cors import CORS

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
CORS(app_views)


# import app_views
from api.v1.views.index import *
from api.v1.views.states import *
