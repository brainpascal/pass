from app.models.product import Product
from app.models.category import Category
from app.models.supplier import Supplier
from app.models.territory import Territory
from app.models.region import Region
from app import db
from sqlalchemy import text

def get_territory_report():
    # Un reporte simple que lista territorios con su región
    return Territory.query.join(Region).add_columns(
        Territory.territoryId,
        Territory.territorydescription,
        Region.regiondescription
    ).all()

def get_products_detailed_report(min_price=20):
    # Query compleja con joins y filtros
    results = (
        db.session.query(
            Product.productId,
            Product.productName,
            Product.unitPrice,
            Category.categoryName,
            Supplier.companyName.label("supplier"),
        )
        .join(Category, Product.categoryId == Category.categoryId)
        .join(Supplier, Product.supplierId == Supplier.supplierId)
        .join(Territory, Supplier.region == Territory.territoryId, isouter=True) 
        .filter(Product.unitPrice >= min_price)
        .order_by(Category.categoryName.asc(), Product.productName.asc())
        .all()
    )
    return results

def product_lista_precios():
    sql = text("""
        SELECT productId, productName, unitPrice
        FROM Product
        WHERE unitPrice >= 10
        ORDER BY unitPrice DESC
    """)
    result = db.session.execute(sql).mappings()
    rows = [dict(row) for row in result]
    return rows



