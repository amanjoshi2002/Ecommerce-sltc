# SLTC Product Distribution Website and App

## Introduction
This project is an internship project aimed at developing a dynamic product distribution website and app using Django, SQLite, Bootstrap, and Flutter. The system enables seamless browsing and ordering for shopkeepers while providing features like product display, ordering system, and direct order input for salesmen.

## Features
- **Product Display**: Browse through a wide range of products available for distribution.
- **Ordering System**: Place orders conveniently through the website or app interface.
- **Direct Order Input**: Salesmen can directly input orders, simplifying the distribution process.
- **User Authentication**: Secure user authentication system for shopkeepers and salesmen.

## Installation
Follow these steps to set up the project locally:

### Prerequisites
- Python 3.x
- Flutter SDK
- SQLite

### Backend (Django)
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sltc-product-distribution.git
   cd sltc-product-distribution/backend
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate  # for Unix/Mac
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Frontend (Flutter)
1. Navigate to the Flutter project directory:
   ```bash
   cd ../frontend
   ```

2. Install dependencies:
   ```bash
   flutter pub get
   ```

3. Run the app:
   ```bash
   flutter run
   ```

## API Routes

### Homepage
- **GET /**: Displays the homepage.
  
### Search
- **GET /search**: Search for products.
  
### Store
- **GET /store**: Displays the store.

### Product View
- **GET /products/{id}**: Displays details of a specific product.

### Signup
- **GET /signup**: Sign up for an account.

### Login
- **GET /login**: Log in to your account.

### Logout
- **GET /logout**: Log out of your account.

### Cart
- **GET /cart**: View and manage your shopping cart.

### Checkout
- **GET /check-out**: Proceed to checkout.

### Orders
- **GET /orders**: View and manage your orders.

### Sales Order Form
- **GET /sales-order/**: Display the sales order form.

### Create Sales Order
- **POST /create-sales-order**: Create a new sales order.

### Search Product
- **GET /search-product**: Search for products.

### Search Retail
- **GET /search-retail**: Search for retail stores.

### Sales Order Success
- **GET /sales-order/success/**: Displays success message after placing a sales order.

## Usage
- Visit the website [SLTC](https://www.sltc.co.in) or launch the app to start browsing products and placing orders.
- Shopkeepers can log in to manage their inventory and orders.
- Salesmen can input orders directly for faster processing.
