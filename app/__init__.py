from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from app.resources.report_resource import ReportResource
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Swagger(app)
    api = Api(app)
    api.add_resource(ReportResource, "/api/report")
    return app
