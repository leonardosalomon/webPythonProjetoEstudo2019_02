#coding: utf-8
from flask import Blueprint, render_template

bp_common = Blueprint('bp_common', __name__, url_prefix='/', template_folder='templates', static_folder='static')

@bp_common.route('/')
def common_index():
    return render_template('common_index.html')

@bp_common.route('/seus-pedidos', methods=['POST'])
def common_requests():
    return render_template('common_requests.html')