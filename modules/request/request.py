#coding: utf-8
from flask import Blueprint, render_template, session, request, redirect, url_for, make_response
from modules.login.login import validateSession
from database.model.PedidoBD import Pedido
from database.model.ProdutoBD import Produto
from database.model.ItemPedBD import ItemPed
from datetime import datetime
import pdfkit

bp_request = Blueprint('bp_request', __name__, url_prefix='/request', template_folder='templates')
itensped = []
produtosped = []

@bp_request.route('/') 
@validateSession
def request_list():
    request = Pedido()
    itensped.clear()
    produtosped.clear()
    requests = request.selectRequestALL()
    return render_template('request_list.html', requests=requests)

@bp_request.route('/create-request', methods=['POST','GET']) 
@validateSession
def request_create():
    tipo = 'Create'
    req = Pedido()
    product = Produto()
    prod= Produto()

    products = product.selectALL()

    itemped = ItemPed()

    temprod = False

    if request.method == 'POST':
        req.data_solicita = datetime.now()
        req.status = 'Pendente'
        req.id_usuario = session['id']

    if itensped != []:
        if 'createRequestDB' in request.form:
            req.insert()
            for ip in itensped:
                ip["id_pedido"] = req.id
                itempedadd = ItemPed()
                itempedadd.id_pedido = req.id
                itempedadd.id_produto = ip.get("id_produto")
                itempedadd.quantidade = ip.get("quantidade")
                itempedadd.quantidade_aprovada = ip.get("quantidade_aprovada")
                itempedadd.insert()
            
            itensped.clear()
            produtosped.clear()

        # return redirect(url_for('bp_request.request_list'))
    if 'addprod' in request.form:
        if itensped != []:
            for ip in itensped:
                if request.form['produto'] == ip.get("id_produto"):
                    temprod = True
        
        if temprod == False and request.form['produto'] != "":

            itemped.id_produto = request.form['produto']
            itemped.quantidade = request.form['quant']
            itemped.quantidade_aprovada = request.form['quant']

            prod.selectONE(itemped.id_produto)

            produtosped.append({"id_produto":itemped.id_produto, "nome":prod.nome, "unidade":prod.unidade, "imagem":prod.imagem, "quantidade":itemped.quantidade})
            itensped.append({"id_produto":itemped.id_produto, "quantidade":itemped.quantidade, "quantidade_aprovada":itemped.quantidade_aprovada, "id_pedido": ""})

    if 'delete' in request.form:
        del itensped[int(request.form['idprod'])-1]
        produtosped.clear()
        for ip in itensped:
            prod.selectONE(ip.get("id_produto"))

            produtosped.append({"id_produto":ip.get("id_produto"), "nome":prod.nome, "unidade":prod.unidade, "imagem":prod.imagem, "quantidade":ip.get("quantidade")})
        #   return redirect(url_for('bp_request.request_list'))
    
    if 'edit' in request.form:
        itensped[int(request.form['idprod'])-1]["quantidade"] = request.form['quant']
        itensped[int(request.form['idprod'])-1]["quantidade_aprovada"] = request.form['quant']
        produtosped.clear()
        for ip in itensped:
            prod.selectONE(ip.get("id_produto"))

            produtosped.append({"id_produto":ip.get("id_produto"), "nome":prod.nome, "unidade":prod.unidade, "imagem":prod.imagem, "quantidade":ip.get("quantidade")})

    if 'cancel' in request.form:
        for ip in itensped:
            print(ip.get("id_produto"))

    return render_template('request_edit.html', tipo=tipo, req=req, products=products, produtosped=produtosped, itensped=itensped
 )

def has_product(pId):
    for pp in produtosped:
        if pp.get('id_produto') == pId:
            return True
    return False

@bp_request.route('/edit-request/<int:id>', methods=['POST', 'GET']) 
@validateSession
def request_edit(id):
    tipo = 'Edit'

    req = Pedido()

    product = Produto()
    
    prod = Produto()

    products = product.selectALL()

    itemped = ItemPed()

    ips = itemped.selectONE(id)

    temprod = False

    for ip in ips:
        prod.selectONE(ip[1])
        if not has_product(ip[1]): 
            produtosped.append({"id_produto":ip[1], "nome":prod.nome, "unidade":prod.unidade, "imagem":prod.imagem, "quantidade":ip[2]})
            itensped.append({"id_produto":ip[1], "quantidade":ip[2], "quantidade_aprovada":ip[6], "id_pedido": ip[0]})

    

    if itensped != []:
        if 'updateRequestDB' in request.form:
            req.delete(id)
            if request.method == 'POST':
                req.data_solicita = datetime.now()
                req.status = 'Pendente'
                req.id_usuario = session['id']
            req.insert()
            for ip in itensped:
                ip["id_pedido"] = req.id
                itempedadd = ItemPed()
                itempedadd.id_pedido = req.id
                itempedadd.id_produto = ip.get("id_produto")
                itempedadd.quantidade = ip.get("quantidade")
                itempedadd.quantidade_aprovada = ip.get("quantidade_aprovada")
                itempedadd.insert()
            
            itensped.clear()
            produtosped.clear()

    if 'addprod' in request.form:
        for ip in itensped:
            if request.form['produto'] == ip.get("id_produto"):
                temprod = True
        
        if temprod == False and request.form['produto'] != "":

            itemped.id_produto = request.form['produto']
            itemped.quantidade = request.form['quant']
            itemped.quantidade_aprovada = request.form['quant']

            prod.selectONE(itemped.id_produto)

            produtosped.append({"id_produto":itemped.id_produto, "nome":prod.nome, "unidade":prod.unidade, "imagem":prod.imagem, "quantidade":itemped.quantidade})
            itensped.append({"id_produto":itemped.id_produto, "quantidade":itemped.quantidade, "quantidade_aprovada":itemped.quantidade_aprovada, "id_pedido": ""})

    if 'edit' in request.form:
        itensped[int(request.form['idprod'])-1]["quantidade"] = request.form['quant']
        itensped[int(request.form['idprod'])-1]["quantidade_aprovada"] = request.form['quant']
        produtosped.clear()
        for ip in itensped:
            prod.selectONE(ip.get("id_produto"))

            produtosped.append({"id_produto":ip.get("id_produto"), "nome":prod.nome, "unidade":prod.unidade, "imagem":prod.imagem, "quantidade":ip.get("quantidade")})

    if 'delete' in request.form:
        del itensped[int(request.form['idprod'])-1]
        produtosped.clear()
        for ip in itensped:
            prod.selectONE(ip.get("id_produto"))

            produtosped.append({"id_produto":ip.get("id_produto"), "nome":prod.nome, "unidade":prod.unidade, "imagem":prod.imagem, "quantidade":ip.get("quantidade")})

    if 'cancel' in request.form:
        for ip in itensped:
            print(ip.get("id_produto"))

    return render_template('request_edit.html', itensped=itensped, produtosped=produtosped, products=products, request=request, tipo=tipo)

@bp_request.route('/delete-request/<int:id>', methods=['POST', 'GET']) 
@validateSession
def request_delete(id):
    tipo = 'delete'

    request = Pedido()

    request.delete(id)
    return redirect(url_for('bp_request.request_list'))

@bp_request.route('/report/<int:id>')
def report(id): 

    ped = Pedido()
    ret = ped.selectRequest(id)
    if not ped.id:
        flash(ret, 'info')
        return redirect(url_for('bp_request.request_list'))

    ped_p = ItemPed()
    products = ped_p.selectONE(id)
    # images = []
    # for product in products:
    #     images.append(product[7])

    ren = render_template('pedido_pdf.html', products=products, ped=ped)
    pdf = pdfkit.from_string(ren, False)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachement; filename=relatorio-pedido.pdf'
    return response