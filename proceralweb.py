import os
import sys
path = os.path.dirname(sys.argv[0])
print(path)
html = os.listdir(f"{path}/html")
css = os.listdir(f"{path}/css")

from http.server import SimpleHTTPRequestHandler, HTTPServer

# Custom handler class to serve "Hello, World!" at /test
class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Check if the request path is /test
        paths = f"{self.path}.html"
        if paths.replace("/","") in html:
            # Respond with a 200 status code



            self.send_response(200)
            # html loading
            try:
                h = open(f"{path}/html/{self.path}.html")
                ch = h.read()
            except:
                ch = ""

            try:
                c = open(f"{path}/html/nav.html")
                nav = c.read()
            except:
                nav=""
                print("no all.css found, skiping")

            #css loading
            
            try:
                c = open(f"{path}/css/{self.path}.css")
                cc = c.read()
            except:
                cc = ""
            try:
                c = open(f"{path}/css/all.css")
                ccss = c.read()
            except:
                print("no all.css found, skiping")
           
            #JS LOADING
            try:
                c = open(f"{path}/script/{self.path}.js")
                js = c.read()
            except:
                js=""
                print("no all.css found, skiping")

            try:
                c = open(f"{path}/script/all.js")
                ajs = c.read()
            except:
                ajs=""
                print("no all.css found, skiping")



            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            # The content of the webpage
            content = f"""<html>
            <style>
            {ccss}
            </style>
            <style>
            {cc}
            
            
            </style>
            <script>
            {ajs}
            </script>
            <script>
            {js}
            </script>
            
            {nav}
            {ch}
            
            
            
            """
            
            # Write the content to the response
            self.wfile.write(content.encode())
        else:
            print(paths.replace("/",""))
            # If the 
            # path is not /test, return a 404 Not Found response
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")

# Set the server address and port
server_address = ('', 8080)

# Create the HTTP server
httpd = HTTPServer(server_address, MyHandler)

# Serve the webpage
print("Serving on port 8080...")
httpd.serve_forever()
