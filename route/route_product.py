from flask import Blueprint, make_response, request, jsonify
from flask_expects_json import expects_json

from controller.controller_product import ControllerProduct
from schema.schema_product import create_product, add_product

controller = ControllerProduct()

url_product = Blueprint('url_product', __name__)

@url_product.route('/product/create', methods = ['POST'])
@expects_json(create_product)
def create():

    json_request = request.json

    response = controller.create(json = json_request)

    return make_response(jsonify(response), response['code'])


@url_product.route('/product/add', methods = ['POST'])
@expects_json(add_product)
def add():

    json_request = request.json

    response = controller.add(json = json_request)

    return make_response(jsonify(response), response['code'])



@url_product.route('/product/all', methods = ['GET'])
def get_all():

    response = controller.get_all()

    return make_response(jsonify(response), response['code'])



@url_product.route('/product/<uid>', methods = ['GET'])
def get_product_branch(uid):

    response = controller.get_by_branch(uid = uid)

    return make_response(jsonify(response), response['code'])



@url_product.route('/product/expired/<uid>', methods = ['GET'])
def check_expired(uid):

    response = controller.check_expired_products(branch = uid)

    return make_response(jsonify(response), response['code'])