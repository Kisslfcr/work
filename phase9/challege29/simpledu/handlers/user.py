from flask import Blueprint, render_template
from simpledu.models import User, Course

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/<username>')
def user_index(username):
    userg = User.query.filter_by(username=username).first_or_404()
    courses = Course.query.filter_by(author_id=userg.id).all()
    return render_template('user/detail.html', userg=userg, courses=courses)

