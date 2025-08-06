from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()        # ← Esto es importante
migrate = Migrate()      # ← Esto también

def create_app():
    app = Flask(__name__)
    # app.config['SECRET_KEY'] = 'secreto123'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flaskuser:flaskpass@localhost/flaskapp'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usuarionorth:FlaskPass123!!@localhost/Northwind'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # para levantar una variable desde .env
    # app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Inicializar DB y migraciones
    db.init_app(app)
    migrate.init_app(app, db)
    
    # from .models import *  # O tus modelos explícitos

    from app.routes.product_routes import product_bp
    app.register_blueprint(product_bp)

    from app.routes.region_routes import region_bp
    app.register_blueprint(region_bp)

    from app.routes.category_routes import category_bp
    app.register_blueprint(category_bp)

    from app.routes.territory_routes import territory_bp
    app.register_blueprint(territory_bp)

    from app.routes.report_routes import report_bp
    app.register_blueprint(report_bp)

    from app.routes.supplier_routes import supplier_bp
    app.register_blueprint(supplier_bp)     

    #from app.routes.salesorder_routes import salesorder_bp
    #app.register_blueprint(salesorder_bp)

    @app.route('/')
    def home():
        return render_template('home.html')

    return app