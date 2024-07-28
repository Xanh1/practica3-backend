from flask import Blueprint, make_response, request, jsonify
from flask_expects_json import expects_json

from controller.controller_user import ControllerUser
from schema.schema_user import save_user, auth_user

controller = ControllerUser()
url_user = Blueprint('url_user', __name__)

@url_user.route('/user/create', methods = ['POST'])
@expects_json(save_user)
def create():

    json_request = request.json

    response = controller.create(json = json_request)

    return make_response(jsonify(response), response['code'])

@url_user.route('/user/auth', methods = ['POST'])
@expects_json(auth_user)
def auth():

    json_request = request.json

    response = controller.auth(json = json_request)

    return make_response(jsonify(response), response['code'])

@url_user.route('/user/<uid>', methods = ['GET'])
def get_user(uid):

    response = controller.get_user_by_uid(uid = uid)

    return make_response(jsonify(response), response['code'])