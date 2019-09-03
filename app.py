#coding: utf-8
from flask import Flask

from mod_common import common_routes
from mod_admin import admin_routes

def create_app():
    app = Flask(__name__)

    app.register_blueprint(admin_routes.admin_bp)
    app.register_blueprint(common_routes.common_bp)

    return app
