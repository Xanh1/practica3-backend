from model.models import Person, Account
from controller.errors.error import json_response, Error
from controller.util.token import create_token

from app import DB

class ControllerUser():

    def create(self, json):

        user = Person()

        user.dni = json['dni']
        user.name = json['name']
        user.last_name = json['last-name']

        account = Account()

        account.username = json['username']
        account.password = json['password']

        user.account = account

        DB.session.add(user)
        DB.session.add(account)
        DB.session.commit()

        return json_response('Success', 200, {"user": user.name + ' ' + user.last_name})

    def auth(self, json):

        user = Account.query.filter_by(username = json['username']).first()
        
        if not user:
            return json_response('Error', 404, Error.NON_EXISTS_ACCOUNT.value)

        if user.password != json['password']:
            return json_response('Error', 404, Error.NON_EXISTS_ACCOUNT.value)
        
        token = create_token(user.uid, 20)

        context = {
            'token': token,
            'user': user.person.name,
            'uid': user.person.uid,
        }

        return json_response('Success', 200, context)
    
    def update(self, json):
        
        person = Person.query.filter_by(uid = json['person']).first()

        if not person:
            return json_response('Error', 404, Error.NON_EXIST_PERSON.value)
        
        person.dni = json['dni']
        person.name = json['name']
        person.last_name = json['last-name']

        DB.session.commit()

        return json_response('Success', 200, 'Profile updated')
    
    
    def get_user_by_uid(self, uid):

        user = Person.query.filter_by(uid = uid).first()

        return json_response('Success', 200, user.serialize)