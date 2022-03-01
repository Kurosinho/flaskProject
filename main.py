from flask import Blueprint, render_template
from flask_login import current_user
from flask_user import roles_accepted

main = Blueprint('main', __name__)


@main.route('/')
def index():  # put application's code here
    return render_template('index.html')


@main.route('/profile')
@roles_accepted('admin', 'user')
def profile():
    return render_template('profile.html', name=current_user.username)
