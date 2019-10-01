#coding: utf-8
from flask import Blueprint, render_template
from modules.login.login import validateSession

bp_product = Blueprint('bp_product', __name__, url_prefix='/product', template_folder='templates')

@bp_product.route('/') 
@validateSession
def product_list():
    return render_template('product_list.html')

@bp_product.route('/edit-product') 
@validateSession
def product_edit():
    return render_template('product_edit.html')
