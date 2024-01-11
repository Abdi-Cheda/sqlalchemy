from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from app import Base

class Restaurant(Base):
    __tablename__ = 'restaurants'
    
    id = Column(Integer, primary_key=True)
    reviews = relationship("Review", back_populates="restaurant")

    def reviews(self):
        return self.reviews

    def customers(self):
        return set(review.customer for review in self.reviews)
