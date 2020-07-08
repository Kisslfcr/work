from flask import Blueprint, render_template

user = Blueprint('user', __name__, url_prefix='/users')

@user.route('/<username>')
def uuuuser(username):
    pass
