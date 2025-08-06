from flask import Blueprint, render_template, request, redirect, url_for
from app.controllers import supplier_controller

supplier_bp = Blueprint('supplier_bp', __name__)

@supplier_bp.route('/supplier/')
def list_suppliers():
    suppliers = supplier_controller.get_all()
    return render_template('supplier/list.html', suppliers=suppliers)

@supplier_bp.route('/supplier/create', methods=['GET', 'POST'])
def create_supplier():
    if request.method == 'POST':
        supplier_controller.create(request.form)
        return redirect(url_for('supplier_bp.list_suppliers'))
    return render_template('supplier/create.html')

@supplier_bp.route('/supplier/edit/<int:id>', methods=['GET', 'POST'])
def edit_supplier(id):
    supplier = supplier_controller.get_by_id(id)
    if request.method == 'POST':
        supplier_controller.update(id, request.form)
        return redirect(url_for('supplier_bp.list_suppliers'))
    return render_template('supplier/edit.html', supplier=supplier)

@supplier_bp.route('/supplier/delete/<int:id>', methods=['POST'])
def delete_supplier(id):
    supplier_controller.delete(id)
    return redirect(url_for('supplier_bp.list_suppliers'))
