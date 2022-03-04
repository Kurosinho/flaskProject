from app import ma
import models


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = models.User

    id = ma.auto_field()
    name = ma.auto_field()
    password = ma.auto_field()


class PokemonSchema(ma.SQLAlchemySchema):
    class Meta:
        model = models.Pokemon

    id = ma.auto_field()
    name = ma.auto_field()
    owner = ma.auto_field()
