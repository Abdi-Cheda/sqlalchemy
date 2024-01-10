from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from app import Base  # Import Base from the module where it's defined

class Restaurant(Base):
    __tablename__ = 'restaurants'
    
    id = Column(Integer, primary_key=True)
    # Include other columns (e.g., name, address) here
    # For example:
    # name = Column(String)

    # Relationships
    reviews = relationship("Review", back_populates="restaurant")

    def reviews(self):
        # This method should have a different name to avoid conflict with the attribute
        return self.reviews

    def customers(self):
        # This method fetches distinct customers who have reviewed the restaurant
        return set(review.customer for review in self.reviews)
