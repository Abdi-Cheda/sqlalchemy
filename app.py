from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///database.db') # database setup
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


# Adding sample data
# Create instances of Customer, Restaurant, and Review
customer1 = Customer(first_name="John", last_name="Doe")
restaurant1 = Restaurant(name="The Fancy Steakhouse", price=4)
review1 = Review(customer=customer1, restaurant=restaurant1, star_rating=5)

# Add instances to the session
session.add(customer1)
session.add(restaurant1)
session.add(review1)

# Commit the transactions
session.commit()

