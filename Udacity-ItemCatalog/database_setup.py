from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(500), nullable=False)
    email = Column(String(500), nullable=False)
    menu_item = relationship('MenuItem', cascade='all, delete-orphan')

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'email': self.email
        }


class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(500))
    price = Column(String(8))
    course = Column(String(500))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    email = Column(String(500), nullable=False)
    restaurant = relationship(Restaurant)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
            'email': self.email
        }


#engine = create_engine('sqlite:///restaurantmenu.db')
engine = create_engine('postgresql://catalog:root123@localhost/catalog1')

Base.metadata.create_all(engine)
