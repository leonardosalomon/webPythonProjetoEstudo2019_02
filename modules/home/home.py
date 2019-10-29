#coding: utf-8
from flask import Blueprint, render_template
from modules.login.login import validateSession

bp_home = Blueprint('bp_home', __name__,
                      url_prefix='/home', template_folder='templates')

@bp_home.route('/', methods=['GET','POST'])
@validateSession
def home():
    return render_template('home.html')
