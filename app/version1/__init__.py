from app.version1.views import MyBlog, SingleBlog

from flask_restful import Api, Resource
from flask import Blueprint

app_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(app_one)

"""adding resources to our endpoints"""
api.add_resource(MyBlog, '/blog')
api.add_resource(SingleBlog, '/blog/<int:blog_id>')
