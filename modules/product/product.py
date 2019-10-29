#coding: utf-8
from flask import Blueprint, render_template, request, redirect, url_for
from modules.login.login import validateSession
from database.model.ProdutoBD import Produto

import base64


bp_product = Blueprint('bp_product', __name__, url_prefix='/product', template_folder='templates')

@bp_product.route('/') 
@validateSession
def product_list():
    product = Produto()

    products = product.selectALL()
    return render_template('product_list.html', products=products)

@bp_product.route('/create-product', methods=['POST','GET']) 
@validateSession
def product_create():
    tipo = 'create'
    product = Produto()

    if request.method == 'POST':
        product.nome = request.form['nome']
        product.unidade = request.form['unidade']
        product.imagem =  "data:" + request.files['imagem'].content_type + ";base64," + str(base64.b64encode( request.files['imagem'].read() ) , "utf-8")
        
    if 'createProductDB' in request.form:
        product.insert()
        return redirect(url_for('bp_product.product_list'))

    if 'cancelProduct' in request.form:
        return redirect(url_for('bp_product.product_list'))

    return render_template('product_edit.html', product=product, tipo=tipo)

@bp_product.route('/edit-product/<int:id>', methods=['POST', 'GET']) 
@validateSession
def product_edit(id):
    tipo = 'edit'

    product = Produto()

    product.selectONE(id)

    if request.method == 'POST':
        product.id = request.form['id']
        product.nome = request.form['nome']
        product.unidade = request.form['unidade']
        product.imagem = "data:" + request.files['imagem'].content_type + ";base64," + str(base64.b64encode( request.files['imagem'].read() ) , "utf-8")
        
        
    if 'editProductDB' in request.form:
        product.update()
        return redirect(url_for('bp_product.product_list'))

    if 'deleteProductDB' in request.form:
        product.delete()
        return redirect(url_for('bp_product.product_list'))
    return render_template('product_edit.html', product=product, tipo=tipo)

@bp_product.route('/delete-user/<int:id>', methods=['POST', 'GET']) 
@validateSession
def product_delete(id):
    tipo = 'delete'

    product = Produto()

    product.delete(id)
    return redirect(url_for('bp_product.product_list'))