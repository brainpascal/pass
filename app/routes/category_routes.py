from flask import Blueprint, render_template, request, redirect, url_for
from app.models.category import Category
from app import db

category_bp = Blueprint('category', __name__, url_prefix='/category')

@category_bp.route('/')
def list():
    categories = Category.query.all()
    return render_template('category/list.html', categories=categories)

@category_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        categoryname = request.form.get('categoryname')
        description = request.form.get('description')
        if categoryname:
            new_category = Category(categoryname=categoryname, description=description)
            db.session.add(new_category)
            db.session.commit()
            return redirect(url_for('category.list'))
    return render_template('category/create.html')

@category_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    category = Category.query.get_or_404(id)
    if request.method == 'POST':
        categoryname = request.form.get('categoryname')
        description = request.form.get('description')
        if categoryname:
            category.categoryname = categoryname
            category.description = description
            db.session.commit()
            return redirect(url_for('category.list'))
    return render_template('category/edit.html', category=category)

@category_bp.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('category.list'))
