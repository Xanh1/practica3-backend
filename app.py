from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

DB = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config = False)
    
    #TODO
    app.config.from_object('config.config.Config')
    
    DB.init_app(app)
    
    with app.app_context():
        from route.route_user import url_user
        from route.route_branch import url_branch
        from route.route_product import url_product
        
        app.register_blueprint(url_user)
        app.register_blueprint(url_branch)
        app.register_blueprint(url_product)
        
        # create db tables
        DB.create_all()
        
        #DB.drop_all()
    
    return app