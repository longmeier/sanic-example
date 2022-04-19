from sanic import Blueprint, Sanic
from .news import *
index_bp = Blueprint('index', url_prefix='/api/index')


index_bp.add_route(bp_root, '/hello/')
index_bp.add_route(get_name, '/get_name/')
index_bp.add_route(get_mobile, '/get_mobile/')
