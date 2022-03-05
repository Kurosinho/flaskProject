from app import ma
import models


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = models.User

    id = ma.auto_field()
    username = ma.auto_field()
    password = ma.auto_field()


class PokemonSchema(ma.SQLAlchemySchema):
    class Meta:
        model = models.Pokemon
        include_fk = True

    id = ma.auto_field()
    name = ma.auto_field()
    owner = ma.auto_field()


user_schema = UserSchema()
users_schema = UserSchema(many=True)

pokemon_schema = PokemonSchema()
pokemons_schema = PokemonSchema(many=True)
