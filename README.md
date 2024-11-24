# Python REST API for Product Management (170186 Kulubya Hassan)

A simple REST API built with Python's built-in http.server module for managing products.

## Setup Instructions

1. Make sure you have Python 3.x installed on your system.

2. Install the required package for the client script: 
bash
pip install requests


## Running the Server

1. Start the server by running:
bash
python product_server.py
The server will start on port 8000.

## Running the Client

1. In a separate terminal, run the client script:
bash
python client.py


## API Endpoints

### POST /products
Creates a new product.

Request body example:

```json
{
    "name": "Laptop",
    "description": "High-performance laptop",
    "price": 999.99
}
```

### GET /products
Retrieves all products.

## Testing Manually

You can test the API using curl:
bash

## Add a product
curl -X POST -H "Content-Type: application/json" -d '{"name":"Test Product","description":"Test Description","price":19.99}' http://localhost:8000/products

## Get all products
curl http://localhost:8000/products


## Error Handling

- 201: Product created successfully
- 400: Invalid request (missing fields or invalid data)
- 404: Endpoint not found
