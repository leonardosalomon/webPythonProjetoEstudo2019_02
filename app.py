#coding: utf-8
from flask import Flask, redirect

from mod_common.common_routes import bp_common
from mod_admin.admin_routes import bp_admin
from mod_error.error import bp_error

def create_app():
    app = Flask(__name__)

    app.register_blueprint(bp_admin)
    app.register_blueprint(bp_common)
    app.register_blueprint(bp_error)

    @app.errorhandler(404)
    def notFound(error):
        return redirect("/error/404",code=302)

    @app.errorhandler(500)
    def serverError(error):
        return redirect("/error/500",code=302), 500

    return app
