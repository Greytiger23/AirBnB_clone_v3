#!/usr/bin/python3
""" int it file"""


from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from .index import *

#import app_views after defining it
from api.v1.views import app_views
