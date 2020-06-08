from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cookie_index.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['name']
        reps = make_response(user)
        reps.set_cookie('name',user) 
        return reps



@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('name')
    return '<h1>welcome, '+name+'</h1>'

