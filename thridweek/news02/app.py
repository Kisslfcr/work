from flask import Flask, render_template, abort
import os, json

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/shiyanlou'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app=app)


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

@app.route('/')
def index():
        jsonshi = File.query.filter(File.id==1).first()        
        jsonhel = File.query.filter(File.id==2).first()        
        return render_template('index.html', jsonshi=jsonshi, jsonhel=jsonhel)
                            
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
