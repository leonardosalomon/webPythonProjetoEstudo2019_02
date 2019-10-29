#coding: utf-8
from flask import Blueprint, render_template, request, redirect, url_for
from modules.login.login import validateSession
from database.model.UsuarioBD import Usuario
import pymysql

bp_user = Blueprint('bp_user', __name__, url_prefix='/user', template_folder='templates')

@bp_user.route('/') 
@validateSession
def user_list():
    user = Usuario()

    users = user.selectUserALL()

    return render_template('user_list.html', users=users, content_type='application/json')

@bp_user.route('/create-user', methods=['POST','GET']) 
@validateSession
def user_create():
    tipo = 'create'
    user = Usuario()

    if request.method == 'POST':
        user.nome = request.form['nome']
        user.cpf = request.form['cpf']
        user.data_nasc = request.form['data_nasc']
        user.sexo = request.form['sexo']
        user.email = request.form['email']
        user.telefone = request.form['telefone']
        user.celular = request.form['celular']
        user.username = request.form['username']
        user.senha = request.form['senha']
        user.setor = request.form['setor']
        user.permissao = request.form['permissao']
        
    if 'createUserDB' in request.form:
        user.insertUser()
    
        return redirect(url_for('bp_user.user_list'))

    return render_template('user_edit.html', user=user, tipo=tipo)

@bp_user.route('/edit-user/<int:id>', methods=['POST', 'GET']) 
@validateSession
def user_edit(id):
    tipo = 'edit'

    user = Usuario()

    user.selectUser(id)

    if request.method == 'POST':
        user.id = request.form['id']
        user.nome = request.form['nome']
        user.cpf = request.form['cpf']
        user.data_nasc = request.form['data_nasc']
        user.sexo = request.form['sexo']
        user.email = request.form['email']
        user.telefone = request.form['telefone']
        user.celular = request.form['celular']
        user.username = request.form['username']
        user.senha = request.form['senha']
        user.setor = request.form['setor']
        user.permissao = request.form['permissao']
        
    if 'editUserDB' in request.form:
        user.updateUser()
        return redirect(url_for('bp_user.user_list'))

    if 'excluiClienteDB' in request.form:
        user.deleteUser(user.id)
        return redirect(url_for('bp_user.user_list'))
    return render_template('user_edit.html', user=user, tipo=tipo)

@bp_user.route('/delete-user/<int:id>', methods=['POST', 'GET']) 
@validateSession
def user_delete(id):
    tipo = 'delete'

    user = Usuario()

    user.deleteUser(id)
    return redirect(url_for('bp_user.user_list'))
