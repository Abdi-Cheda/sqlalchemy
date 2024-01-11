from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///database.db') # Database setup
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Customer(Base): # Model Definitions
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def reviews(self):
        return session.query(Review).filter(Review.customer_id == self.id).all()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    def reviews(self):
        return session.query(Review).filter(Review.restaurant_id == self.id).all()

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    star_rating = Column(Integer)
    customer = relationship("Customer")
    restaurant = relationship("Restaurant")

Base.metadata.create_all(engine) # Create tables