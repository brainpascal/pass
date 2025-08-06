from flask import Blueprint, render_template, request, redirect, url_for
from app.models.region import Region
from app import db

region_bp = Blueprint('region', __name__, url_prefix='/region')

@region_bp.route('/')
def list():
    regions = Region.query.all()
    return render_template('region/list.html', regions=regions)

@region_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        description = request.form.get('regiondescription')
        if description:
            new_region = Region(regiondescription=description)
            db.session.add(new_region)
            db.session.commit()
            return redirect(url_for('region.list'))
    return render_template('region/create.html')

@region_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    region = Region.query.get_or_404(id)
    if request.method == 'POST':
        description = request.form.get('regiondescription')
        if description:
            region.regiondescription = description
            db.session.commit()
            return redirect(url_for('region.list'))
    return render_template('region/edit.html', region=region)

@region_bp.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    region = Region.query.get_or_404(id)
    db.session.delete(region)
    db.session.commit()
    return redirect(url_for('region.list'))
