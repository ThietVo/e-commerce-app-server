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

p11 = Products(
    productName='productName11',
    image='',
    price='100',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p12 = Products(
    productName='productName12',
    image='',
    price='200',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p13 = Products(
    productName='productName13',
    image='',
    price='300',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p14 = Products(
    productName='productName14',
    image='',
    price='400',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p15 = Products(
    productName='productName15',
    image='',
    price='500',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p16 = Products(
    productName='productName16',
    image='',
    price='600',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p17 = Products(
    productName='productName17',
    image='',
    price='700',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p18 = Products(
    productName='productName18',
    image='',
    price='800',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p19 = Products(
    productName='productName19',
    image='',
    price='900',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p20 = Products(
    productName='productName20',
    image='',
    price='1000',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)

p21 = Products(
    productName='productName10',
    image='',
    price='1000',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)

p22 = Products(
    productName='productName11',
    image='',
    price='100',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p23 = Products(
    productName='productName12',
    image='',
    price='200',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p24 = Products(
    productName='productName13',
    image='',
    price='300',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p25 = Products(
    productName='productName14',
    image='',
    price='400',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p26 = Products(
    productName='productName15',
    image='',
    price='500',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p27 = Products(
    productName='productName16',
    image='',
    price='600',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p28 = Products(
    productName='productName17',
    image='',
    price='700',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p29 = Products(
    productName='productName18',
    image='',
    price='800',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)
p30 = Products(
    productName='productName19',
    image='',
    price='900',
    unit='each',
    sale='yes',
    created_at=func.now(),
    updated_at=func.now()
)

db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])
db.session.add_all([p11, p12, p13, p14, p15, p16, p17, p18, p19, p20])
db.session.add_all([p21, p22, p23, p24, p25, p26, p27, p28, p29, p30])

db.session.commit()