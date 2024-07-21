from http.server import BaseHTTPRequestHandler, HTTPServer

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/healthz':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.end_headers()

def run_health_check_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, HealthCheckHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    run_health_check_server()
