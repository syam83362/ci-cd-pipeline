from http.server import BaseHTTPRequestHandler, HTTPServer


def hello():
	return "Hello from CI/CD!"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Docker!")

if __name__ == "__main__":
	server = HTTPServer(("0.0.0.0", 8000), Handler)
	server.serve_forever()
	print("server is running on port 8000")
	server.serve_forever()
