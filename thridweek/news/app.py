from flask import Flask, render_template, abort
import os, json

app = Flask(__name__)

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
