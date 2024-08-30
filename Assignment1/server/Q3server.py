import http.server
import socketserver
import os

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Set the directory to serve files from
        self.directory = 'www'
        super().__init__(*args, **kwargs)

def run_server(port=8000):
    # Set the port to listen on
    handler = MyHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving HTTP on port {port}...")
        httpd.serve_forever()

run_server()