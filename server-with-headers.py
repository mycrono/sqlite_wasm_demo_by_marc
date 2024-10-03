import http.server
from http.server import SimpleHTTPRequestHandler

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add the custom headers
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        # Call the superclass's method to complete the headers
        super().end_headers()

if __name__ == "__main__":
    # Define the server, binding to localhost on port 8080
    server_address = ("127.0.0.1", 8080)
    httpd = http.server.HTTPServer(server_address, CustomHTTPRequestHandler)
    print("Serving on http://127.0.0.1:8080")
    httpd.serve_forever()
