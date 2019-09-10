#coding: utf-8
from flask import Blueprint, render_template

bp_admin = Blueprint('bp_admin', __name__, url_prefix='/admin', template_folder='templates', static_folder='static')

@bp_admin.route('/lista-pedidos') 
def admin_list_requests():
    return render_template('admin_list_requests.html')

@bp_admin.route('/edit-pedidos') 
def admin_edit_requests():
    return render_template('admin_requests.html')

@bp_admin.route('/fornecedores') 
def admin_providers():
    return render_template('admin_providers.html')

@bp_admin.route('/seus-pedidos') 
def admin_your_requests():
    return render_template('admin_your_requests.html')

@bp_admin.route('/lista-produtos') 
def admin_list_products():
    return render_template('admin_list_products.html')

@bp_admin.route('/edit-produtos') 
def admin_edit_products():
    return render_template('admin_products.html')

@bp_admin.route('/lista-usuarios') 
def admin_list_users():
    return render_template('admin_list_users.html')

@bp_admin.route('/edit-usuarios') 
def admin_edit_users():
    return render_template('admin_users.html')
