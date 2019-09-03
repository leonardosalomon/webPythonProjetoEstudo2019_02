#coding: utf-8
from flask import Blueprint, render_template

admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin', template_folder='templates', static_folder='static')

@admin_bp.route('/pedidos') 
def admin_requests():
    return render_template('admin_requests.html')

@admin_bp.route('/fornecedores') 
def admin_providers():
    return render_template('admin_providers.html')

@admin_bp.route('/seus-pedidos') 
def admin_your_requests():
    return render_template('admin_your_requests.html')

@admin_bp.route('/produtos') 
def admin_products():
    return render_template('admin_products.html')

@admin_bp.route('/usuarios') 
def admin_users():
    return render_template('admin_users.html')
