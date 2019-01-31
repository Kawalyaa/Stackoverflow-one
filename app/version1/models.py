from flask import request, make_response, jsonify
import datetime
import time
blog_list = []
date_and_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')


class MyBlogModel():
    def __init__(self):
        self.db = blog_list
        self.dt = date_and_time

    def add_blog(self, tittle, description):
        data = {
            'blog_id': len(self.db) + 1,
            'tittle': tittle,
            'description': description,
            'date_and_time': self.dt
        }
        self.db.append(data)
        return self.db

    def get_blogs(self):
        return self.db

    def get_one(self, blog_id):
        for blog in self.db:
            if blog['blog_id'] == blog_id:
                return make_response(jsonify({"blog": blog}), 200)
        return make_response(jsonify({
            "message": 'blog id not found'
        }), 404)

    def update_blog(self, blog_id):
        req = request.get_json()
        for ablog in self.db:
            if ablog['blog_id'] == blog_id:
                ablog['tittle'] = req['tittle']
                ablog['description'] = req['description']
                return make_response(jsonify({"ablog": ablog}), 200)

        create_one = {
            "blog_id": blog_id,
            "tittle": req['tittle'],
            "description": req['description'],
            "updated_time": self.dt
        }
        self.db.append(create_one)
        return make_response(jsonify({
            "updated_blog": create_one
        }), 201)

    def delete_one(self, blog_id):
        for ablog in self.db:
            if ablog['blog_id'] == blog_id:
                self.db.remove(ablog)
                return make_response(jsonify({"message": 'blog with id {} is deleted'.format(blog_id)}), 200)
        return make_response(jsonify({"message": 'Blog id is not found'}), 404)
