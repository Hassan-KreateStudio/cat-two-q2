import requests
import json

def add_product(name, description, price):
    url = 'http://localhost:8000/products'
    product = {
        'name': name,
        'description': description,
        'price': price
    }
    
    response = requests.post(url, json=product)
    print(f'Status Code: {response.status_code}')
    print(f'Response: {response.json()}')

def get_products():
    url = 'http://localhost:8000/products'
    response = requests.get(url)
    print(f'Status Code: {response.status_code}')
    print('Products:')
    print(json.dumps(response.json(), indent=2))

if __name__ == '__main__':
    # Add some sample products
    add_product('Laptop', 'High-performance laptop', 999.99)
    add_product('Mouse', 'Wireless mouse', 29.99)
    
    # Get all products
    get_products() 