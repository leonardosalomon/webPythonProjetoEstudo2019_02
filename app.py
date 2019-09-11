#coding: utf-8
from flask import Flask, redirect

from mod_common.common_routes import bp_common
from mod_admin.admin_routes import bp_admin
from mod_error.error import bp_error
from mod_login.login import bp_login

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'you-will-never-guess'

    app.register_blueprint(bp_admin)
    app.register_blueprint(bp_common)
    app.register_blueprint(bp_error)
    app.register_blueprint(bp_login)

    @app.errorhandler(404)
    def notFound(error):
        return redirect("/error/404",code=302)

    @app.errorhandler(500)
    def serverError(error):
        return redirect("/error/500",code=302), 500

    return app
