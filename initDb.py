from src import db
from src.models import Products
from sqlalchemy.sql import func

db.drop_all()
db.create_all()

p1 = Products(
    productName='productName1',
    image='',
    price='100',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p2 = Products(
    productName='productName2',
    image='',
    price='200',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p3 = Products(
    productName='productName3',
    image='',
    price='300',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p4 = Products(
    productName='productName4',
    image='',
    price='400',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p5 = Products(
    productName='productName5',
    image='',
    price='500',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p6 = Products(
    productName='productName6',
    image='',
    price='600',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p7 = Products(
    productName='productName7',
    image='',
    price='700',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p8 = Products(
    productName='productName8',
    image='',
    price='800',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p9 = Products(
    productName='productName9',
    image='',
    price='900',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p10 = Products(
    productName='productName10',
    image='',
    price='1000',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)

db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])

db.session.commit()