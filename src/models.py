from . import db
from sqlalchemy.sql import func

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.String(100), nullable=False)
    unit = db.Column(db.String(255), nullable=False)
    sale = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

