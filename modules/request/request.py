#coding: utf-8
from flask import Blueprint, render_template

bp_request = Blueprint('bp_request', __name__, url_prefix='/request', template_folder='templates')

@bp_request.route('/') 
def request_list():
    return render_template('request_list.html')

@bp_request.route('/edit-request') 
def request_edit():
    return render_template('request_edit.html')
