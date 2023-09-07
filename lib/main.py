from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review

# Create the database engine
engine = create_engine('sqlite:///restaurant_reviews.db')

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

def main():
    # Sample queries and interactions

    # Query all restaurants and print their names
    all_restaurants = session.query(Restaurant).all()
    print("All Restaurants:")
    for restaurant in all_restaurants:
        print(f"{restaurant.name} - Price: {restaurant.price}")

    # Query all customers and print their names
    all_customers = session.query(Customer).all()
    print("\nAll Customers:")
    for customer in all_customers:
        print(f"{customer.first_name} {customer.last_name}")

    # Get the fanciest restaurant
    fanciest_restaurant = Restaurant.fanciest()
    print(f"\nFanciest Restaurant: {fanciest_restaurant.name}")

    # Add a new review
    customer = session.query(Customer).filter_by(first_name="John").first()
    restaurant = session.query(Restaurant).filter_by(name="Restaurant A").first()
    new_review = customer.add_review(restaurant, 5)
    session.commit()

    # Query the reviews for Restaurant A
    reviews_for_restaurant_a = restaurant.reviews()
    print("\nReviews for Restaurant A:")
    for review in reviews_for_restaurant_a:
        print(review.full_review())

    # Delete all reviews for Restaurant B
    customer2 = session.query(Customer).filter_by(first_name="Jane").first()
    restaurant2 = session.query(Restaurant).filter_by(name="Restaurant B").first()
    customer2.delete_reviews(restaurant2)
    session.commit()

    # Query the reviews for Restaurant B (after deletion)
    reviews_for_restaurant_b = restaurant2.reviews()
    print("\nReviews for Restaurant B (after deletion):")
    for review in reviews_for_restaurant_b:
        print(review.full_review())

if __name__ == "__main__":
    main()
