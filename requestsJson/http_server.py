import http.server
import socketserver

PORT = 8080

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as http_server:
    print(f'HTTP server started {PORT}')
    http_server.serve_forever()