#coding: utf-8
from flask import Blueprint, render_template, request, redirect, url_for, flash
'''from wtforms import Form, BooleanField, StringField, PasswordField, validators'''
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

bp_login = Blueprint('bp_login', __name__, url_prefix='/', template_folder='templates')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

@bp_login.route('/index') 
def logins():
    return render_template('formLogin.html')

'''@bp_login.route('/register', methods=['POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    else:
        return render_template('teste.html', form=form)
        

@bp_login.route('/') 
def logoff():
    return render_template('formLogin.html')'''

@bp_login.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect( url_for('bp_common.common_index') )
        '''if form.username.data == 'abc' and form.password.data == 'Bolinhas':
            return redirect( url_for('bp_common.common_index') )'''
    return render_template('login.html', title='Sign In', form=form)
    