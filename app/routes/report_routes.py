from flask import Blueprint, render_template, request
from app.controllers import report_controller

report_bp = Blueprint('report', __name__, url_prefix='/report')

@report_bp.route('/')
def index():
    return render_template('report/index.html')

@report_bp.route('/territories')
def territory_report():
    data = report_controller.get_territory_report()
    return render_template('report/territory_report.html', data=data)


@report_bp.route('/products-complex')
def product_report():
    # Tomar parámetro opcional min_price
    try:
        min_price = float(request.args.get('min_price', 20))
    except ValueError:
        min_price = 20
    data = report_controller.get_products_detailed_report(min_price)
    return render_template('report/complex_product_report.html', data=data, min_price=min_price)


@report_bp.route('/product_lista_precios')
def product_lista_precios():
    data = report_controller.product_lista_precios()
    return render_template('report/product_lista_precios.html', data=data)
