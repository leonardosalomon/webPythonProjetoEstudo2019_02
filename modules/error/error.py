#coding: utf-8
from flask import Blueprint, render_template

bp_error = Blueprint('bp_error', __name__, url_prefix='/error', template_folder='templates')

@bp_error.route('/404')
def notFound():
    return render_template("form404.html"), 404

@bp_error.route('/500')
def serverError():
    return render_template("form500.html"), 500
