from flask import Flask,render_template
from flask import url_for
from flask import redirect
from flask import request
from flask import session
from datetime import timedelta
from flask import make_response

app = Flask(__name__)

#set session
@app.route('/set_session')
def set_session():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)
    session['username'] = 'shiyanlou'
    return 'set session successfully'

# get session
@app.route('/get_session')
def get_session():
    value = session.get('username')
    return 'get session {}'.format(value)
#remove session
@app.route('/del_session')
def del_session():
    value = session.pop('username')
    return 'remove session successfully, session is {}'.format(value)


@app.route('/')
def index():
    course = {
            'python': 'lou+ python',
            'java': 'java base',
            'bigdata': 'spark sql',
            'teacher': 'shixiaolou',
            'is_unique':False,
            'has_tag':True,
            'tags':['c','c++','docker']
            }
    return render_template('index.html',course=course)

@app.route('/user/<username>')
def user_index(username):
    resp = make_response(render_template('user_index.html', username=username))
    resp.set_cookie('username',username)
#    print('User-Agent:',request.headers.get('User-Ageng'))
#    print('time:', request.args.get('time'))
#    print('q:', request.args.get('q'))
#    print('Q:', request.args.getlist('Q'))
    return resp

@app.route('/register',methods=['GET', 'POST'])
def register():
    print('method:',request.method)
    print('name:', request.form.get('name'))
    print('password:', request.form.get('password'))
    print('hobbies:', request.form.getlist('hobbies'))
    print('age:', request.form.get('age', default=18))
    return 'registered successfully!'

@app.route('/httptest',methods=['GET', 'POST'])
def httptest():
    if request.method == 'GET':
        print('method:',request.method)
        print('t:', request.args.get('t'))
        print('q:', request.args.get('q'))
        return 'It is a get request!'
    elif request.method == 'POST':
        print('method:',request.method)
        print('-------------', request.form.getlist.__doc__)
        print('Q:', request.form.getlist('Q'))
        return 'It is a post request!'

@app.route('/post/<post_id>')
def show_post(post_id):
    return post_id


@app.route('/test')
def test():
    # 第一个参数字符串是视图函数的名字
    # 后面的参数都是带名字的，也就是关键字参数，它们作为视图函数的参数使用
    print(url_for('courses',name='java'))
#    print(url_for('show_post',post_id=1,_external=True))
#    print(url_for('show_post',post_id=2,q='python 03'))
#    print(url_for('show_post',post_id=2,q='python can'))
#    print(url_for('show_post',post_id=2,_anchor='a'))
    return 'Hello Shiyanlou!'

'''
@app.route('/<username>')
def hello(username):
    if username == 'shixiaolou':
        return 'hello {}'.format(username)
    else:
        return redirect(url_for('index'))
'''

@app.route('/courses/<name>')
def Courses(name):
    return 'Course: {}!'.format(name)
#    return  render_template('user_index.html',coursename = name)

# 用户主页的视图函数
@app.route('/<username>/index')
@app.route('/user_index/<username>')
def uuser_index(username):
    # 这个 if 假装是判断用户的登录状态，如果处于登录状态，显示用户主页
    if username == 'Admin':
        return 'Admin 的个人主页'
    # 如果没有处于登录状态，就把 username 当作课程名字，返回课程页
#    return redirect(url_for('.courses', name=username))
    return redirect('https://www.baidu.com')

if __name__ == '__main__':
    app.run()
