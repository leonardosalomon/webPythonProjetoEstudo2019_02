#coding: utf-8
from flask import Blueprint, render_template
from modules.login.login import validateSession

bp_user = Blueprint('bp_user', __name__, url_prefix='/user', template_folder='templates')

@bp_user.route('/') 
@validateSession
def user_list():
    return render_template('user_list.html')

@bp_user.route('/edit-user') 
@validateSession
def user_edit():
    return render_template('user_edit.html')
