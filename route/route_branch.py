from flask import Blueprint, make_response, request, jsonify
from flask_expects_json import expects_json

from controller.controller_branch import ControllerBranch
from schema.schema_branch import create_branch

controller = ControllerBranch()

url_branch = Blueprint('url_branch', __name__)

@url_branch.route('/branch/create', methods = ['POST'])
@expects_json(create_branch)
def create():

    json_request = request.json

    response = controller.create(json = json_request)

    return make_response(jsonify(response), response['code'])
