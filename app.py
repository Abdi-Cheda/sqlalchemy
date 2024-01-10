from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Database Setup
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Model Definitions
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    # Define other columns as needed

    def reviews(self):
        return session.query(Review).filter(Review.customer_id == self.id).all()

    # Include other methods here

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    # Define other columns as needed

    def reviews(self):
        return session.query(Review).filter(Review.restaurant_id == self.id).all()

    # Include other methods here

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    star_rating = Column(Integer)

    customer = relationship("Customer")
    restaurant = relationship("Restaurant")

    # Include other methods here

# Create tables
    from sqlalchemy import create_engine

# data models

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

