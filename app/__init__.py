from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()        # ← Esto es importante
migrate = Migrate()      # ← Esto también

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secreto123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flaskuser:flaskpass@localhost/flaskapp'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # para levantar una variable desde .env
    # app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Inicializar DB y migraciones
    db.init_app(app)
    migrate.init_app(app, db)
    # from .models import *  # O tus modelos explícitos

    from app.routes.product_routes import product_bp
    app.register_blueprint(product_bp)

    @app.route('/')
    def home():
        return render_template('home.html')

    return app