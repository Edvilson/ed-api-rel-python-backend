from flask import Flask
from flasgger import Swagger
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from routes.relatorio_routes import relatorio_bp

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///relatorios.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Swagger(app)
app.register_blueprint(relatorio_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
