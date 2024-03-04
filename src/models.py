from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites = db.relationship('Favorites', back_populates='user')

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    img = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String(), unique=True, nullable=False)

    characters = db.relationship('Character', back_populates='item')
    planets = db.relationship('Planet', back_populates='item')
    vehicles = db.relationship('Vehicle', back_populates='item')
    favorites = db.relationship('Favorites', back_populates='item')

class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    birth_year = db.Column(db.String(100), unique=True, nullable=False)
    gender = db.Column(db.String(100), unique=True, nullable=False)
    height = db.Column(db.String(100), unique=True, nullable=False)
    hair_color = db.Column(db.String(100), unique=True, nullable=False)
    eye_color = db.Column(db.String(100), unique=True, nullable=False)

    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    item = db.relationship('Item', back_populates='characters')
    favorites = db.relationship('Favorites', back_populates='characters')

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }
     
class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    climate = db.Column(db.String(100), unique=True, nullable=False)
    diameter = db.Column(db.String(100), unique=True, nullable=False)
    gravity = db.Column(db.String(100), unique=True, nullable=False)
    population = db.Column(db.String(100), unique=True, nullable=False)
    terrain = db.Column(db.String(100), unique=True, nullable=False)

    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    item = db.relationship('Item', back_populates='planets')
    favorites = db.relationship('Favorites', back_populates='planets')

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }

class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    description = db.Column(db.String(100), unique=True, nullable=False)
    model_name = db.Column(db.String(100), unique=True, nullable=False)
    manufacturer = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.String(100), unique=True, nullable=False)
    length = db.Column(db.String(100), unique=True, nullable=False)
    
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    item = db.relationship('Item', back_populates='vehicles')
    favorites = db.relationship('Favorites', back_populates='vehicles')

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='favorites')

    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    planets = db.relationship('Planet', back_populates='favorites')

    characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    characters = db.relationship('Character', back_populates='favorites')

    vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    vehicles = db.relationship('Vehicle', back_populates='favorites')
    
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    item = db.relationship('Item', back_populates='favorites')

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planets_id": self.planets_id,
            "characters_id": self.characters_id,
            "vehicles_id": self.vehicles_id,
        }