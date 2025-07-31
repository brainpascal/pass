from flask import Blueprint, render_template, request, redirect, url_for
from app.controllers.product_controller import *

product_bp = Blueprint('product', __name__, url_prefix='/products')

@product_bp.route('/')
def list_products():
    products = get_all_products()
    return render_template('product/list.html', products=products)

@product_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        data = {
            'productName': request.form['productName'],
            'supplierId': request.form.get('supplierId') or None,
            'categoryId': request.form.get('categoryId') or None,
            'quantityPerUnit': request.form.get('quantityPerUnit'),
            'unitPrice': request.form.get('unitPrice') or None,
            'unitsInStock': request.form.get('unitsInStock') or None,
            'unitsOnOrder': request.form.get('unitsOnOrder') or None,
            'reorderLevel': request.form.get('reorderLevel') or None,
            'discontinued': request.form['discontinued']
        }
        create_product(data)
        return redirect(url_for('product.list_products'))
    return render_template('product/create.html')

@product_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    product = get_product_by_id(id)
    if request.method == 'POST':
        data = {
            'productName': request.form['productName'],
            'supplierId': request.form.get('supplierId') or None,
            'categoryId': request.form.get('categoryId') or None,
            'quantityPerUnit': request.form.get('quantityPerUnit'),
            'unitPrice': request.form.get('unitPrice') or None,
            'unitsInStock': request.form.get('unitsInStock') or None,
            'unitsOnOrder': request.form.get('unitsOnOrder') or None,
            'reorderLevel': request.form.get('reorderLevel') or None,
            'discontinued': request.form['discontinued']
        }
        update_product(product, data)
        return redirect(url_for('product.list_products'))
    return render_template('product/edit.html', product=product)

@product_bp.route('/delete/<int:id>')
def delete(id):
    product = get_product_by_id(id)
    delete_product(product)
    return redirect(url_for('product.list_products'))
