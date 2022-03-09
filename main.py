import json

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
    pokemons = get_all_pokemon()
    return render_template('profile.html', name=current_user.username, pokemons=pokemons)


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
    pokemons = pokemons_schema.dump(all_pokemon)
    # pokemons = json.loads(result)
    # pokemons = json.loads(jsonified)
    return pokemons


@main.route('/get_pokemon/<id>', methods=['GET'])
def get_pokemon(id):
    pokemon = Pokemon.query.get(id)

    return pokemon_schema.jsonify(pokemon)


@main.route('/remove_pokemon/<id>', methods=['DELETE'])
def remove_pokemon(id):
    pokemon = Pokemon.query.get_or_404(id)
    db.session.delete(pokemon)
    db.session.commit()

    return 'Successfully removed a pokemon', 204
