#coding: utf-8
from flask import Blueprint, render_template

bp_product = Blueprint('bp_product', __name__, url_prefix='/product', template_folder='templates')

@bp_product.route('/') 
def product_list():
    return render_template('product_list.html')

@bp_product.route('/edit-product') 
def product_edit():
    return render_template('product_edit.html')
