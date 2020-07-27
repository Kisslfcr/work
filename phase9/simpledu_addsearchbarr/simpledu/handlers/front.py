from flask import flash, Blueprint, render_template, redirect, url_for
from flask import request, current_app
from flask_login import login_user, logout_user, login_required

from simpledu.models import Course, User
from simpledu.forms import LoginForm, RegisterForm


front = Blueprint('front', __name__)


@front.route('/')
def index():
    page = request.args.get('page', default=1, type=int)
    pagination = Course.query.paginate(
            page=page,
            per_page=current_app.config['INDEX_PER_PAGE'],
            error_out=False
            )
    return render_template('index.html', pagination=pagination)


@front.route('/search')
def search():
    search_str = request.args.get('search').strip()
    page = request.args.get('page', default=1, type=int)
    if len(search_str) < 2:
        flash('Content bu neng xiao yu 2.', 'warning')
        q = Course.query.filter_by(id=0)
    else:
        flash('Result ru xia.', 'success')
        q = Course.query.whooshee_search(search_str)
    pagination = q.paginate(
            page=page,
            per_page=current_app.config['INDEX_PER_PAGE'],
            error_out=False
    )
    return render_template('index.html', pagination=pagination)


@front.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print('----------form:', form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            flash('Email not exists.', 'info')
            return redirect(url_for('.login'))
        if not user.check_password(form.password.data):
            flash('username or passwor is not correct', 'warning')
            return redirect(url_for('.login'))
        flash('Login success!', 'success')
        login_user(user, form.remember_me.data)
        return redirect(url_for('.index'))
    return render_template('login.html', form=form)

@front.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已经退出登录','success')
    return redirect(url_for('.index'))

@front.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功，清登录!', 'success')
        return redirect(url_for('.login'))
    return render_template('register.html', form=form)
