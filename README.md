 Welcome to the Pizza Ordering System, a Django-based web application that allows users to customize and order their pizzas online. The system manages user accounts, pizza customization, delivery details, and order tracking, providing a seamless experience from account creation to order confirmation. Additionally, it features an admin interface for managing pizza options such as sizes, cheeses, and sauces.

Table of Contents

1. Features
2. Installation
3. Usage
4. Admin Features
5. Tech Stack
6. Screenshots
7. Contributing


Features
User-Facing Features
User Registration & Authentication: Users can create an account, log in, and manage their orders.
Order History: View all previous pizza orders upon login.
Pizza Customization: Users can build a pizza by selecting:
Pizza size (small, medium, large, etc.)
Crust type (normal, thin, thick, gluten-free)
Sauce (tomato, BBQ)
Cheese (Mozzarella, Vegan, Low fat)
Toppings (e.g., pepperoni, chicken, mushrooms, onions, etc.)
Delivery Details: Enter delivery and payment information, with form validation to ensure accurate inputs.
Order Confirmation: View a summary of the pizza ordered, including delivery details and estimated time.
Admin Features
Manage Pizza Options: Admins can add, update, or delete pizza sizes, cheeses, and sauces via the Django admin interface.
Installation
To run this project locally, follow these steps:

Prerequisites
Python 3.8 or above
Django 4.1 or above
pip (Python package manager)

Steps
1. Clone the Repository

bash
Copy code
git clone https://github.com/your-username/pizza-ordering-system.git
cd pizza-ordering-system

2. Create a Virtual Environment

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

bash
Copy code
pip install -r requirements.txt
4. Migrate the Database

bash
Copy code
python manage.py migrate

5. Create a Superuser

bash
Copy code
python manage.py createsuperuser

6. Run the Development Server

bash
Copy code
python manage.py runserver

7. Open your browser and navigate to http://127.0.0.1:8000/ to access the app.

Usage
User Workflow
Create an Account: Sign up to access the pizza ordering system.
View Orders: After login, view previous orders or start a new pizza order.
Customize Your Pizza: Choose size, crust, sauce, cheese, and toppings to build your pizza.
Enter Delivery & Payment Info: Provide your name, address, and payment details (credit card info with validation).
Confirm Your Order: After successfully submitting your details, the system displays your pizza order and delivery information.
Admin Workflow
Log in to the Admin Panel: Access the admin panel at /admin to manage pizza options.
Add/Remove Pizza Sizes, Cheeses, and Sauces: Easily update or delete pizza options from the admin interface.
Admin Features
Through the Django admin interface, administrators can:

Add New Pizza Sizes: Define new pizza sizes that users can select.
Add New Cheese Types: Provide additional cheese options such as vegan or special types.
Add New Sauces: Add new sauces like pesto or white garlic sauce.
Tech Stack
Backend: Django (Python)
Frontend: HTML, CSS, JavaScript (Bootstrap for styling)
Database: SQLite (default Django database)
Forms: Django forms with built-in validation
Screenshots
User Dashboard

Pizza Customization Page

Order Confirmation

Admin Panel

Contributing
Contributions are welcome! If you’d like to contribute, please follow these steps:

Fork the repository.
Create a new branch for your feature (git checkout -b feature-branch).
Make your changes and commit (git commit -m "Add new feature").
Push to the branch (git push origin feature-branch).
Create a pull request.
