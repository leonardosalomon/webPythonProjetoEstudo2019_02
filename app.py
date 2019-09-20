#coding: utf-8
from flask import Flask, redirect, session, url_for
from datetime import timedelta

import os

from modules.login.login import bp_login
from modules.home.home import bp_home
from modules.error.error import bp_error
from modules.user.user import bp_user
from modules.product.product import bp_product
from modules.request.request import bp_request

def create_app():
    app = Flask(__name__)
    '''app.config['SECRET_KEY'] = 'you-will-never-guess'''
    app.secret_key = os.urandom(12).hex()

    app.register_blueprint(bp_login)
    app.register_blueprint(bp_home)
    app.register_blueprint(bp_error)
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_product)
    app.register_blueprint(bp_request)

    @app.before_request
    def before_request():
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=15)
        time = app.permanent_session_lifetime

    @app.errorhandler(404)
    def notFound(error):
        return redirect("/error/404",code=302)

    @app.errorhandler(500)
    def serverError(error):
        return redirect("/error/500",code=302), 500

    return app
