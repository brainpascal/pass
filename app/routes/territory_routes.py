from flask import Blueprint, render_template, request, redirect, url_for
from app.models.territory import Territory
from app.models.region import Region
from app import db

territory_bp = Blueprint('territory', __name__, url_prefix='/territory')

@territory_bp.route('/')
def list():
    territories = Territory.query.all()
    return render_template('territory/list.html', territories=territories)

@territory_bp.route('/create', methods=['GET', 'POST'])
def create():
    regions = Region.query.all()
    if request.method == 'POST':
        territoryid = request.form.get('territoryid')
        territorydescription = request.form.get('territorydescription')
        regionid = request.form.get('regionid')

        if territoryid and territorydescription and regionid:
            new_territory = Territory(
                territoryid=territoryid,
                territorydescription=territorydescription,
                regionid=int(regionid)
            )
            db.session.add(new_territory)
            db.session.commit()
            return redirect(url_for('territory.list'))

    return render_template('territory/create.html', regions=regions)

@territory_bp.route('/edit/<string:id>', methods=['GET', 'POST'])
def edit(id):
    territory = Territory.query.get_or_404(id)
    regions = Region.query.all()

    if request.method == 'POST':
        territoryid = request.form.get('territoryid')
        territorydescription = request.form.get('territorydescription')
        regionid = request.form.get('regionid')

        if territoryid and territorydescription and regionid:
            territory.territoryid = territoryid
            territory.territorydescription = territorydescription
            territory.regionid = int(regionid)
            db.session.commit()
            return redirect(url_for('territory.list'))

    return render_template('territory/edit.html', territory=territory, regions=regions)

@territory_bp.route('/delete/<string:id>', methods=['POST'])
def delete(id):
    territory = Territory.query.get_or_404(id)
    db.session.delete(territory)
    db.session.commit()
    return redirect(url_for('territory.list'))
