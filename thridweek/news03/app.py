from flask import Flask, render_template, abort
import os, json
from pymongo import MongoClient


app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/shiyanlou'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
client = MongoClient('localhost',27017)
mong = client.shiyanlou


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '<Category: {}>'.format(self.name)

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    content = db.Column(db.Text)
    category = db.relationship('Category', backref='files')
    def __init__(self,title,created_time,category,content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content
    def __repr__(self):
        return '<File: {}>'.format(self.title)

    def add_tag(self, tag_name):
        tag_item = mong.tag.find_one({'fileid':self.id})
        if tag_item:
            tags = tag_item['tag']
            if tag_name not in tags:
                tags.append(tag_name)
                mong.tag.update_one({'fileid':self.id},{'$set':{'tag':tags}})
        else:
            tags = [tag_name]
            mong.tag.insert_one({'fileid':self.id,'tag':tags})
        return tags

    def remove_tag(self, tag_name):
        tag_item = mong.tag.find_one({'fileid':self.id})
        if tag_item:
            tags = tag_item['tag']
            if tag_name in tags:
                tags.remove(tag_name)
                mong.tag.update_one({'fileid':self.id},{'$set':{'tag':tags}})
                return tags
            else:
                return tags
        else:
            return[]

    @property
    def tags(self):
        tag_item = mong.tag.find_one({'fileid':self.id})
        if tag_item:
            return tag_item['tag']
        return []
        
@app.route('/')
def index():
        jsonshi = File.query.filter(File.id==1).first()        
        jsonhel = File.query.filter(File.id==2).first()        
        tags11 = mong.tag.find_one({'fileid':1})
        tags1 = tags11['tag']
        tags22 = mong.tag.find_one({'fileid':2})  
        tags2 = tags22['tag']
        return render_template('index.html', jsonshi=jsonshi, jsonhel=jsonhel,tags1=tags1,tags2=tags2)
                            
@app.route('/files/<filename>')
def file(filename):
    jsonf = File.query.filter(File.id==filename).first()
    if jsonf:
        return render_template('file.html', jsonf=jsonf)
    else:
        abort(404)

@app.errorhandler(404)
def not_found(error):
        return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
