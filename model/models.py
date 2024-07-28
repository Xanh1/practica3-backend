from app import DB
import uuid, enum
from datetime import date

'''
    Product Models
'''

class Product(DB.Model):
    
    # table name
    __tablename__ = 'products'
    
    # fields
    id          = DB.Column(DB.Integer, primary_key=True)
    uid         = DB.Column(DB.String(60), default=str(uuid.uuid4()), nullable=False)
    name        = DB.Column(DB.String(60), nullable=False, unique=True)
    description = DB.Column(DB.String(100), nullable=False)
    
    # parent relationships 
    batches = DB.relationship('Batch', back_populates='product')
    
    # child relationships
    
    # metodos
    @property
    def serialize(self):
        return {
            'uid'        : self.uid,
            'name'       : self.name,
            'description' : self.description,
        }


class ProductStatus(enum.Enum):

    FRESH = 'Fresh'
    NEAR_EXPIRY = 'Near_Expiry'
    EXPIRED = 'Expired'


class Batch(DB.Model):
    
    # table name
    __tablename__ = 'batches'
    
    # fields
    id         = DB.Column(DB.Integer, primary_key = True)
    uid        = DB.Column(DB.String(60), default = str(uuid.uuid4()), nullable = False)
    price      = DB.Column(DB.Float, nullable = False)
    stock      = DB.Column(DB.Integer, default = 0, nullable = False)
    exp_date   = DB.Column(DB.Date, nullable = False)
    status     = DB.Column(DB.Enum(ProductStatus), nullable = False, default = ProductStatus.FRESH.value)
    product_id = DB.Column(DB.Integer, DB.ForeignKey('products.id'), nullable = False)
    branch_id  = DB.Column(DB.Integer, DB.ForeignKey('branches.id'), nullable=False)
    
    # relationships
    product = DB.relationship('Product', back_populates = 'batches', uselist = False)
    branch  = DB.relationship('Branch', back_populates = 'batches', uselist = False)
    
    # methods
    @property
    def serialize(self):
        return {
            'uid'      : self.uid,
            'product'  : self.product.name,
            'price'    : self.price,
            'stock'    : self.stock,
            'exp_date' : self.exp_date,
            'status'   : self.status.value,
            'branch'   : self.branch.name,
        }

    
    def update_status(self):
        
        current_date = date.today()
        
        days_left = (self.exp_date - current_date).days

        if days_left <= 0:
            self.status = ProductStatus.EXPIRED.value
        elif days_left <= 5:
            self.status = ProductStatus.NEAR_EXPIRY.value
        else:
            self.status = ProductStatus.FRESH.value



'''
    Branch Models
'''

class Branch(DB.Model):

    # table name
    __tablename__ = 'branches'

    # fields
    id        = DB.Column(DB.Integer, primary_key = True)
    uid       = DB.Column(DB.String(60), default = str(uuid.uuid4()), nullable = False)
    name      = DB.Column(DB.String(10), nullable = False, unique = True)
    longitude = DB.Column(DB.Float, nullable=False)
    latitude  = DB.Column(DB.Float, nullable=False)

    # relationships
    batches = DB.relationship('Batch', back_populates='branch')

    # methods
    @property
    def serialize(self):
        return {
            'uid'       : self.uid,
            'name'      : self.name,
            'longitude' : self.longitude,
            'latitude'  : self.latitude,
        }


'''
    User Models
'''

class Person(DB.Model):
    
    # table name
    __tablename__ = 'people'
    
    # fields
    id        = DB.Column(DB.Integer, primary_key = True)
    uid       = DB.Column(DB.String(60), default = str(uuid.uuid4()), nullable = False)
    dni       = DB.Column(DB.String(10), nullable = False, unique = True)
    name      = DB.Column(DB.String(50), nullable = False)
    last_name = DB.Column(DB.String(50), nullable = False)
    
    # parent relationships
    account = DB.relationship('Account', back_populates = 'person', uselist=False)
    
    # child relationships
    
    # methods
    @property
    def serialize(self):
        return {
            'uid'       : self.uid,
            'dni'       : self.dni,
            'name'      : self.name,
            'last_name' : self.last_name,
        }


class Account(DB.Model):
    
    # table name
    __tablename__ = 'accounts'
    
    # fields
    id        = DB.Column(DB.Integer, primary_key = True)
    uid       = DB.Column(DB.String(60), default = str(uuid.uuid4()), nullable = False)
    username  = DB.Column(DB.String(255), nullable = False, unique = True)
    password  = DB.Column(DB.String(50), nullable = False)
    person_id = DB.Column(DB.Integer, DB.ForeignKey('people.id'), nullable = False, unique = True)
    
    # parents relationships
    
    # child relationships
    person = DB.relationship('Person', back_populates = 'account', uselist=False)
    
    # methods
    @property
    def serialize(self):
        return {
            'uid'       : self.uid,
            'username'  : self.username,
            'password'  : self.password,
            'name'      : self.person.name,
            'last_name' : self.person.last_name,
        }


