from model.models import Branch
from controller.errors.error import Error, json_response

from app import DB

class ControllerBranch():

    def get_all(self):

        branches = Branch.query.all()

        return json_response('Success', 200, [branch.serialize for branch in branches])
    
    def create(self, json):

        name = Branch.query.filter_by(name = json['name']).first()

        if name:
            return json_response('Error', 409, Error.BRANCH_EXIST.value)
        
        branch = Branch()

        branch.name = json['name'] 
        branch.latitude = json['latitude'] 
        branch.longitude = json['longitude'] 

        DB.session.add(branch)
        DB.session.commit()

        return json_response('Success', 200, 'Branch created')


    def get_by_uid(self, uid):
        return Branch.query.filter_by(uid = uid).first()