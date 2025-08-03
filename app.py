from flask import Flask
from flasgger import Swagger
from dotenv import load_dotenv
import os
from config.settings import Config
from routes.relatorio_routes import relatorio_bp
from models.relatorio import db

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
Swagger(app)

app.register_blueprint(relatorio_bp)

if __name__ == '__main__':
    app.run(debug=True)
