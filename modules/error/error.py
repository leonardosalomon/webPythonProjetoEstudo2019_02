#coding: utf-8
from flask import Blueprint, render_template
from modules.login.login import validateSession

bp_error = Blueprint('bp_error', __name__, url_prefix='/error', template_folder='templates')

@bp_error.route('/404')
@validateSession
def notFound():
    return render_template("form404.html"), 404

@bp_error.route('/500')
@validateSession
def serverError():
    return render_template("form500.html"), 500
