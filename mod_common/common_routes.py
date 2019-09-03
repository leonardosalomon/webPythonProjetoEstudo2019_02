#coding: utf-8
from flask import Blueprint, render_template

common_bp = Blueprint('common_bp', __name__, url_prefix='/', template_folder='templates', static_folder='static')

@common_bp.route('/')
def common_index():
    return render_template('common_index.html')

@common_bp.route('/seus-pedidos')
def common_requests():
    return render_template('common_requests.html')