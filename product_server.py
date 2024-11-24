from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# In-memory storage for products
products = []

class ProductHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        if self.path == '/products':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                product = json.loads(post_data.decode('utf-8'))
                
                # Validate required fields
                if not all(key in product for key in ['name', 'description', 'price']):
                    self._set_headers(400)
                    response = {'error': 'Missing required fields'}
                    self.wfile.write(json.dumps(response).encode('utf-8'))
                    return

                # Validate price is float
                if not isinstance(product['price'], (int, float)):
                    self._set_headers(400)
                    response = {'error': 'Price must be a number'}
                    self.wfile.write(json.dumps(response).encode('utf-8'))
                    return

                products.append(product)
                self._set_headers(201)
                self.wfile.write(json.dumps(product).encode('utf-8'))
            
            except json.JSONDecodeError:
                self._set_headers(400)
                response = {'error': 'Invalid JSON'}
                self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self._set_headers(404)
            response = {'error': 'Not found'}
            self.wfile.write(json.dumps(response).encode('utf-8'))

    def do_GET(self):
        if self.path == '/products':
            self._set_headers(200)
            self.wfile.write(json.dumps(products).encode('utf-8'))
        else:
            self._set_headers(404)
            response = {'error': 'Not found'}
            self.wfile.write(json.dumps(response).encode('utf-8'))

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, ProductHandler)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server() 