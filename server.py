from http.server import SimpleHTTPRequestHandler, HTTPServer
from gpiozero import LED

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/led/on':
            print("Request Received!")
        self.send_response(200)
        self.end_headers()

httpd = HTTPServer(("",8080),MyHandler)
httpd.serve_forever()
