from flask import Blueprint, render_template, request, redirect, url_for
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


@main.route('/add_pokemon', methods=['GET'])
def get_add_pokemon():
    return render_template('new_pokemon.html')


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
@roles_accepted('admin')
def get_all_pokemon():
    all_pokemon = Pokemon.query.all()
    pokemons = pokemons_schema.dump(all_pokemon)

    return pokemons


@main.route('/pokemon/<username>', methods=['GET'])
@roles_accepted('admin', 'user')
def get_pokemon_by_user(username):
    users_pokemon = Pokemon.query.get(username)
    users_pokemons = pokemons_schema.dump(users_pokemon)

    return users_pokemons


@main.route('/get_pokemon/<owner>', methods=['GET'])
def get_pokemon_by_owner(owner):
    owners_pokemon = Pokemon.query.get(owner)
    pokemons = pokemons_schema.dump(owners_pokemon)

    return pokemons


@main.route('/get_pokemon/<id>', methods=['GET'])
def get_pokemon(id):
    pokemon = Pokemon.query.get(id)

    return pokemon_schema.jsonify(pokemon)


@main.route('/remove_pokemon/<id>', methods=['POST'])
def remove_pokemon(id):
    pokemon = Pokemon.query.get_or_404(id)
    db.session.delete(pokemon)
    db.session.commit()

    return redirect(url_for('main.profile'))
