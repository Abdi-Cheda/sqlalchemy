from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    # Include other columns (e.g., name, email) here
    # For example:
    # name = Column(String)

    # Relationships
    reviews = relationship("Review", back_populates="customer")

