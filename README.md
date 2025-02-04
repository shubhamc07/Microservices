# E-Commerce Microservices POC

This is a **Proof of Concept (POC)** demonstrating a microservices-based e-commerce system using Django. It consists of three microservices: **User Service, Product Service, and Order Service**, along with an **API Gateway** that acts as a single entry point for all client requests.

## 🚀 Project Structure
```
/microservices-poc/
│── api_gateway/          # API Gateway to route requests to microservices
│── user_service/         # User authentication & profile management
│── product_service/      # Product inventory management
│── order_service/        # Order management & transactions
│── manage.py             # Django project management script
│── requirements.txt      # Python dependencies
│── README.md             # Project documentation
```

## 📌 Microservices Overview

### 1️⃣ **User Service** (`user_service`)
- Handles **User Registration & Authentication** using JWT.
- API Endpoints:
  - `POST /api/users/register/` – Register a new user
  - `POST /api/users/login/` – Authenticate and generate JWT token

### 2️⃣ **Product Service** (`product_service`)
- Manages **products & inventory**.
- API Endpoints:
  - `GET /api/products/` – Fetch all products
  - `POST /api/products/` – Add a new product

### 3️⃣ **Order Service** (`order_service`)
- Handles **order creation & tracking**.
- API Endpoints:
  - `POST /api/orders/` – Place a new order
  - `GET /api/orders/` – List all orders

### 4️⃣ **API Gateway** (`api_gateway`)
- Routes requests to appropriate microservices.
- API Endpoints:
  - `POST /users/register/` → Routes to `user_service`
  - `GET /products/` → Routes to `product_service`
  - `POST /orders/` → Routes to `order_service`

## 🔧 Setup & Installation

### **1. Clone the Repository**
```sh
git clone https://github.com/your-repo/microservices-poc.git
cd microservices-poc
```

### **2. Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4. Configure Environment Variables**
Create a `.env` file in the root directory and define the microservice URLs:
```env
USER_SERVICE_URL=http://127.0.0.1:8001/api/users/
PRODUCT_SERVICE_URL=http://127.0.0.1:8002/api/products/
ORDER_SERVICE_URL=http://127.0.0.1:8003/api/orders/
```

### **5. Run Microservices**
Start each microservice on a different port:
```sh
# Run User Service
cd user_service
python manage.py runserver 8001

# Run Product Service
cd ../product_service
python manage.py runserver 8002

# Run Order Service
cd ../order_service
python manage.py runserver 8003
```

### **6. Run API Gateway**
```sh
cd ../api_gateway
python manage.py runserver 8000
```
Now, all requests can be made to `http://127.0.0.1:8000/`.

## 🔒 Authentication & JWT Usage
- After logging in, the user receives a JWT token.
- Include this token in the `Authorization` header for secure API access:
```sh
Authorization: Bearer <your_jwt_token>
```




