from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, DateField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired, Optional

class OrderDetailForm(FlaskForm):
    productId = IntegerField('Producto ID', validators=[DataRequired()])
    unitPrice = DecimalField('Precio Unitario', validators=[DataRequired()])
    quantity = IntegerField('Cantidad', validators=[DataRequired()])
    discount = DecimalField('Descuento', validators=[DataRequired()])

class SalesOrderForm(FlaskForm):
    custId = IntegerField('Cliente ID', validators=[DataRequired()])
    employeeId = IntegerField('Empleado ID', validators=[Optional()])
    orderDate = DateField('Fecha Pedido', validators=[Optional()])
    requiredDate = DateField('Fecha Requerida', validators=[Optional()])
    shippedDate = DateField('Fecha Envío', validators=[Optional()])
    shipperid = IntegerField('Shipper ID', validators=[DataRequired()])
    freight = DecimalField('Flete', validators=[Optional()])
    shipName = StringField('Nombre envío', validators=[Optional()])
    shipAddress = StringField('Dirección envío', validators=[Optional()])
    shipCity = StringField('Ciudad', validators=[Optional()])
    shipRegion = StringField('Región', validators=[Optional()])
    shipPostalCode = StringField('Código Postal', validators=[Optional()])
    shipCountry = StringField('País', validators=[Optional()])

    details = FieldList(FormField(OrderDetailForm), min_entries=1)
    submit = SubmitField('Guardar Pedido')
