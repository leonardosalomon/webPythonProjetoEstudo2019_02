#coding: utf-8
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from functools import wraps

bp_login = Blueprint('bp_login', __name__, url_prefix='/',
                     template_folder='templates')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw = { 'placeholder':'Usuário' })
    password = PasswordField('Password', validators=[DataRequired()], render_kw = { 'placeholder':'Senha' })
    '''remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')'''

# valida se o usuário esta ativo na sessão
def validateSession(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
        #descarta os dados copiados da função original e retorna a tela de login
            return redirect(url_for('bp_login.login', falhaSessao=1))
        else:
        #retorna os dados copiados da função original
            return f(*args, **kwargs)
    #retorna o resultado do if acima
    return decorated_function

@bp_login.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        '''flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('bp_common.common_index'))'''
        error = None
        if form.username.data == 'abc' and form.password.data == 'Bolinhas':
            session.clear()
            session['usuario'] = form.username.data
            return redirect(url_for('bp_home.home'))
        else:
            error = 'Invalid Credentials'
            flash(error)
    return render_template('formLogin.html', title='Sign In', form=form)

@bp_login.route('/logoff', methods=['GET', 'POST'])
def logoff():
    #limpa um valor individual'''
    #session.pop('usuario',None)'''

    #limpa toda a sessão
    session.clear()
    return redirect(url_for('bp_login.login'))
