from model.models import Product, Batch, ProductStatus
from controller.errors.error import Error, json_response
from controller.controller_branch import ControllerBranch
from app import DB

ctr_branch = ControllerBranch()

class ControllerProduct():

    def get_all(self):

        self.check_status()
        
        products = Batch.query.filter(Batch.status != ProductStatus.EXPIRED.value).all()

        return json_response('Success', 200, [product.serialize for product in products])
    
    
    
    def create(self, json):

        name = Product.query.filter_by(name = json['name']).first()

        if name:
            return json_response('Error', 409, Error.PRODUCT_EXISTS.value)
        
        product = Product()

        product.name = json['name']
        product.description = json['description']

        DB.session.add(product)
        DB.session.commit()

        return json_response('Success', 200, 'Product created')
    
    
    
    def add(self, json):

        branch = ctr_branch.get_by_uid(uid = json['branch'])

        if not branch:
            return json_response('Error', 404, Error.NON_EXIST_BRANCH.value)
        
        product = Product.query.filter_by(uid = json['product']).first()

        if not product:
            return json_response('Error', 404, Error.NON_EXIST_PRODUCT.value)
        
        batch = Batch()

        batch.price = json['price']
        batch.stock = json['stock']
        batch.exp_date = json['exp_date']
        batch.branch = branch
        batch.product = product

        product.batches.append(batch)
        branch.batches.append(batch)

        DB.session.add(batch)
        DB.session.commit()

        return json_response('Success', 200, 'Product added')
    
    
    
    def get_by_branch(self, uid):

        branch = ctr_branch.get_by_uid(uid)

        if not branch:
            return json_response('Error', 404, Error.NON_EXIST_BRANCH.value)
        
        self.check_status()

        batches = Batch.query.filter_by(branch_id = branch.id).all()

        return json_response('Success', 200, [batch.serialize for batch in batches])
    


    def check_status(self):
        
        batches = Batch.query.all()
        
        for batch in batches:
            
            batch.update_status()
        
        DB.session.commit()


    def check_expired_products(self, branch):

        batches = Batch.query.filter_by(status = ProductStatus.EXPIRED.value).all()

        for batch in batches:
            if batch.branch.uid == branch:
                return json_response('Success', 200, 'Exist expired products')
        
        
        return json_response('Success', 200, 'has not expired products')
    
