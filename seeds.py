from app import session, Customer, Restaurant, Review

# Create sample data
customer1 = Customer(name="John Doe")
# Create instances and add them to the session
restaurant1 = Restaurant(name="The Fancy Steakhouse", price=4)
customer1 = Customer(first_name="John", last_name="Doe")

session.add(restaurant1)
session.add(customer1)
session.commit()

# Create a Review instance
review1 = Review(restaurant_id=restaurant1.id, customer_id=customer1.id, star_rating=5)

session.add(review1)
session.commit()
