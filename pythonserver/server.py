from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class S198_Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        print self.path
        f = open(curdir + sep + "index.html")
        self.send_response(200)
        self.send_header('Content-type',	'text/html')
        self.end_headers()
        self.wfile.write(f.read())
        self.wfile.write("<p id='username'>"+self.path[1:]+"</p>")
        self.wfile.write("\n</HTML>")
        f.close()
        return
def main():
    try:
        server = HTTPServer(('', 8000), S198_Handler)
        print 'Started Server on port 8000'
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()

if __name__ == "__main__":
    main();