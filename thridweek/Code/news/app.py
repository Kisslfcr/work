from flask import Flask, render_template, abort
import os, json

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/shiyanlou'
db = SQLAlchemy(app=app)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def __repr__(self):
        return 'id:{0},name:{1}'.format(self.id,self.name)

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    #category_id = db.Column(db.Integer,db.ForeignKey(Category.id))
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    content = db.Column(db.Text)
    def __init__(self,id,title,created_time,category_id,content):
        self.id = id
        self.title = title
        self.created_time = created_time
        self.category_id = category_id
        self.content = content
    def __repr__(self):
        return 'id:{0},title:{1},created_time{2},category_id{3},content{4}'.format(self.id,self.title,self.created_time,self.category_id,self.content)

@app.route('/')
def index():
    with open('/home/shiyanlou/files/helloshiyanlou.json') as f:
        jsonshi = json.load(f)
    with open('/home/shiyanlou/files/helloworld.json') as f:
        jsonhel = json.load(f)
    return render_template('index.html', jsonshi=jsonshi, jsonhel=jsonhel)
                            
@app.route('/files/<filename>')
def file(filename):
    if os.path.exists('/home/shiyanlou/files/{}.json'.format(filename)):
        with open('/home/shiyanlou/files/{}.json'.format(filename)) as f:
            jsonf = json.load(f)
        return render_template('file.html', jsonf=jsonf)
    else:
        abort(404)

@app.errorhandler(404)
def not_found(error):
        return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
