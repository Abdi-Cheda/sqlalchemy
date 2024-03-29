# Restaurant Review System
This project is a simple database-driven application for managing restaurant reviews. It uses SQLAlchemy with SQLite for data handling. The application allows users to add customers, restaurants, and their reviews to the database.

## Project Structure
The project is divided into two main parts:
app.py: Contains the database models and the SQLAlchemy session setup.
seeds.py: A script for populating the database with initial data through terminal inputs.

## Models
The application consists of the following models:
Customer: Represents customers with their first and last names.
Restaurant: Represents restaurants, including their name and price level.
Review: Represents reviews, linking customers and restaurants, along with a star rating.

## Usage
Run app.py to create the initial database and tables:
python app.py

## Adding Data to the Database
To add data (customers, restaurants, or reviews), run the seeds.py script:
python seeds.py

Follow the prompts to input data for customers, restaurants, and reviews. Each category is numbered, and you can choose the appropriate number to add data to that category.
As below:
1. Add Customer
2. Add Restaurant
3. Add Review
4. Exit
Enter your choice: 

## Features
Easy Data Input: User-friendly terminal prompts for data entry.
Data Relationship Management: Automatically handles relationships between customers, restaurants, and reviews.
Scalable: Easily extendable for more features or models.

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [https://github.com/Abdi-Cheda/sqlalchemy.git] if you want to contribute.

## Author
ABDIRAHMAN CHEDA

## License
This project is MIT licensed.