#coding: utf-8
from flask import Blueprint, render_template

bp_admin = Blueprint('bp_admin', __name__, url_prefix='/admin', template_folder='templates', static_folder='static')

@bp_admin.route('/pedidos') 
def admin_requests():
    return render_template('admin_requests.html')

@bp_admin.route('/fornecedores') 
def admin_providers():
    return render_template('admin_providers.html')

@bp_admin.route('/seus-pedidos') 
def admin_your_requests():
    return render_template('admin_your_requests.html')

@bp_admin.route('/produtos') 
def admin_products():
    return render_template('admin_products.html')

@bp_admin.route('/usuarios') 
def admin_users():
    return render_template('admin_users.html')
