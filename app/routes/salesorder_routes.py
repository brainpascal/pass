from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models.salesorder import SalesOrder
from app.models.orderdetail import OrderDetail
from app import db

salesorder_bp = Blueprint('salesorder', __name__, url_prefix='/salesorders')

@salesorder_bp.route('/')
def list_salesorders():
    salesorders = SalesOrder.query.all()
    return render_template('salesorders/list.html', salesorders=salesorders)

@salesorder_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Obtener datos del formulario
        custId = request.form.get('custId')
        employeeId = request.form.get('employeeId')
        orderDate = request.form.get('orderDate')
        requiredDate = request.form.get('requiredDate')
        shippedDate = request.form.get('shippedDate')
        shipperid = request.form.get('shipperid')
        freight = request.form.get('freight')
        shipName = request.form.get('shipName')
        shipAddress = request.form.get('shipAddress')
        shipCity = request.form.get('shipCity')
        shipRegion = request.form.get('shipRegion')
        shipPostalCode = request.form.get('shipPostalCode')
        shipCountry = request.form.get('shipCountry')

        # Crear objeto SalesOrder
        new_order = SalesOrder(
            custId=custId,
            employeeId=employeeId if employeeId else None,
            orderDate=orderDate if orderDate else None,
            requiredDate=requiredDate if requiredDate else None,
            shippedDate=shippedDate if shippedDate else None,
            shipperid=shipperid,
            freight=freight if freight else None,
            shipName=shipName,
            shipAddress=shipAddress,
            shipCity=shipCity,
            shipRegion=shipRegion,
            shipPostalCode=shipPostalCode,
            shipCountry=shipCountry
        )

        try:
            db.session.add(new_order)
            db.session.commit()
            flash('Pedido creado exitosamente.', 'success')
            return redirect(url_for('salesorder.list_salesorders'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al crear el pedido: {str(e)}', 'danger')

    return render_template('salesorders/create.html')

@salesorder_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    order = SalesOrder.query.get_or_404(id)

    if request.method == 'POST':
        order.custId = request.form.get('custId')
        order.employeeId = request.form.get('employeeId')
        order.orderDate = request.form.get('orderDate')
        order.requiredDate = request.form.get('requiredDate')
        order.shippedDate = request.form.get('shippedDate')
        order.shipperid = request.form.get('shipperid')
        order.freight = request.form.get('freight')
        order.shipName = request.form.get('shipName')
        order.shipAddress = request.form.get('shipAddress')
        order.shipCity = request.form.get('shipCity')
        order.shipRegion = request.form.get('shipRegion')
        order.shipPostalCode = request.form.get('shipPostalCode')
        order.shipCountry = request.form.get('shipCountry')

        try:
            db.session.commit()
            flash('Pedido actualizado exitosamente.', 'success')
            return redirect(url_for('salesorder.list_salesorders'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar el pedido: {str(e)}', 'danger')

    return render_template('salesorders/edit.html', order=order)

@salesorder_bp.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    order = SalesOrder.query.get_or_404(id)
    try:
        db.session.delete(order)
        db.session.commit()
        flash('Pedido eliminado exitosamente.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar el pedido: {str(e)}', 'danger')

    return redirect(url_for('salesorder.list_salesorders'))
