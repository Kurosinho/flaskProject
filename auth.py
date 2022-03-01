from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user
from flask import current_app

from app import db
from models import User, Role, UserRoles

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET'])
def login():  # put application's code here
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():  # put application's code here
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        flash('Either username or password is incorrect. Try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=True)
    return redirect(url_for('main.profile'))


@auth.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()

    if user:
        flash('Username is taken')
        return redirect(url_for('auth.signup'))

    # if username or password == "": <-- This needs a fix
    #    flash('Username or password cannot be empty!')
    #    return redirect(url_for('auth.signup'))

    with current_app.app_context():
        new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)

        role = Role.query.filter(Role.name == 'user').first()

        if role is None:
            role = Role(name='user')
            db.session.add(role)
            db.session.commit()

        user_role = UserRoles(user_id=new_user.id, role_id=role.id)
        db.session.add(user_role)
        db.session.commit()

    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
