from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_user import UserManager
from werkzeug.security import generate_password_hash
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

from models import User
from models import Role


def create_app():
    myapp = Flask(__name__)

    myapp.config['SECRET_KEY'] = '721309c55afe8d847e992a42'
    myapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    myapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    myapp.config['USER_APP_NAME'] = 'Flask Database Project'
    myapp.config['USER_ENABLE_EMAIL'] = False
    myapp.config['USER_ENABLE_USERNAME'] = True
    myapp.config['USER_REQUIRE_RETYPE_PASSWORD'] = False

    db.init_app(myapp)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(myapp)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from auth import auth as auth_blueprint
    from main import main as main_blueprint

    myapp.register_blueprint(auth_blueprint)
    myapp.register_blueprint(main_blueprint)

    user_manager = UserManager(myapp, db, User)

    with myapp.app_context():
        if not User.query.filter(User.username == 'admin').first():
            user = User(username='admin', password=generate_password_hash('admin', method='sha256'))
            user.roles.append(Role(name='admin'))

            db.session.add(user)
            db.session.commit()

    return myapp


if __name__ == '__main__':
    app = create_app()
    app.run(host='127.0.0.0', port=5000, debug=True)
