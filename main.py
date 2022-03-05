from flask import Blueprint, render_template, request, jsonify
from flask_login import current_user
from flask_user import roles_accepted

from app import db
from models import Pokemon, User
from schemas import pokemon_schema, pokemons_schema

main = Blueprint('main', __name__)


@main.route('/')
def index():  # put application's code here
    return render_template('index.html')


@main.route('/profile')
@roles_accepted('admin', 'user')
def profile():
    return render_template('profile.html', name=current_user.username)


@main.route('/add_pokemon', methods=['POST'])
def add_pokemon():
    name = request.json['name']
    owner = request.json['owner']

    if User.query.filter_by(username=owner).first():
        new_pokemon = Pokemon(name=name, owner=owner)
        db.session.add(new_pokemon)
        db.session.commit()

        return pokemon_schema.jsonify(new_pokemon)

    return "No such user, try again"


@main.route('/get_pokemon', methods=['GET'])
def get_all_pokemon():
    all_pokemon = Pokemon.query.all()
    result = pokemons_schema.dump(all_pokemon)

    return jsonify(result)
