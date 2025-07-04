# Simple E-Commerce API

## Project Overview
The Simple E-Commerce API is a backend service built with Python and Django REST Framework. It allows users to browse products, manage shopping carts, place orders, and view order history. The API is designed with modularity, scalability, and ease of maintenance in mind.

---

## Features
- Browse products and categories
- Manage user shopping cart (add, update, remove items)
- Place orders via a mock checkout
- View order history and order details
- User authentication with token-based authorization (JWT)
- Modular Django apps for products, cart, orders, and users
- RESTful API design
- Data persisted in a relational database (SQLite by default)

---

## Architecture & Folder Structure
- **Products App:** Handles product and category data.
- **Cart App:** Manages shopping cart and cart items.
- **Orders App:** Handles order creation, order items, and order history.
- **Users App (Optional):** Manages user registration, login, and profile.

Each app contains models, serializers, views, URLs, tests, and migrations.  
The main project folder manages global settings, URL routing, and WSGI/ASGI configurations.

---

## API Endpoints

### Products
- `GET /api/products/` — List all products
- `GET /api/products/{id}/` — Get product details by ID
- `GET /api/products/categories/` — List all product categories

### Cart
- `GET /api/cart/` — Get current user's cart contents
- `POST /api/cart/add/` — Add items to cart
- `POST /api/cart/remove/` — Remove items from cart
- `PUT/PATCH /api/cart/update/` — Update item quantities

### Orders
- `POST /api/orders/checkout/` — Checkout current cart and create an order (mock payment)
- `GET /api/orders/` — List user’s order history
- `GET /api/orders/{id}/` — View specific order details

### Users (Optional)
- `POST /api/users/register/` — Register new user
- `POST /api/users/login/` — Login and receive auth token
- `GET/PATCH /api/users/profile/` — View or update user profile

---

## Authentication & Authorization
- Token-based authentication (JWT recommended)
- Only authenticated users can manage carts and place orders
- Product and category data is publicly accessible

---

## Database Design Summary
- **Category:** Product categories (e.g., Electronics, Clothing)
- **Product:** Product details (category, price, stock, description)
- **CartItem:** Links user and products with quantity for shopping cart
- **Order:** Order metadata (user, timestamp)
- **OrderItem:** Links products to orders with quantity and price snapshot
- **User:** Managed by Django’s default or extended user model

---

## Additional Considerations
- Input validation (e.g., stock availability)
- Proper error handling with meaningful HTTP status codes
- Pagination on product listings for performance
- Comprehensive unit and integration tests
- Admin interface available via Django admin

---

## Getting Started

### Prerequisites
- Python 3.x
- pip (Python package manager)
- Virtualenv (recommended)

### Installation
```bash
git clone <repository-url>
cd simple-ecommerce-api
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
