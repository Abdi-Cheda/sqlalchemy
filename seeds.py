from app import session, Customer, Restaurant, Review

def create_customer():
    first_name = input("Enter customer's first name: ")
    last_name = input("Enter customer's last name: ")
    customer = Customer(first_name=first_name, last_name=last_name)
    session.add(customer)
    session.commit()
    print(f"Added customer {first_name} {last_name}")

def create_restaurant():
    name = input("Enter restaurant name: ")
    price = int(input("Enter restaurant price level (1-5): "))
    restaurant = Restaurant(name=name, price=price)
    session.add(restaurant)
    session.commit()
    print(f"Added restaurant {name}")

def create_review():
    customer_id = int(input("Enter customer ID: "))
    restaurant_id = int(input("Enter restaurant ID: "))
    star_rating = int(input("Enter star rating (1-5): "))
    review = Review(customer_id=customer_id, restaurant_id=restaurant_id, star_rating=star_rating)
    session.add(review)
    session.commit()
    print("Added review")

if __name__ == "__main__":
    while True:
        print("1. Add Customer\n2. Add Restaurant\n3. Add Review\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            create_customer()
        elif choice == '2':
            create_restaurant()
        elif choice == '3':
            create_review()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")