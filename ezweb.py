port = 8000

# im sory you have to look at this bad code
import os
import sys
path = os.path.dirname(sys.argv[0])
print(path)
html = os.listdir(f"{path}/html")
css = os.listdir(f"{path}/css")

from http.server import SimpleHTTPRequestHandler, HTTPServer

# main loop
class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # makes index work
        if self.path == "/":
            selfpath = "index"
        else:
            selfpath = self.path

        paths = f"{selfpath}.html"
        if paths.replace("/","") in html:
            
            



            self.send_response(200)
            # html loading
            try:
                h = open(f"{path}/html/{selfpath}.html")
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
                c = open(f"{path}/css/{selfpath}.css")
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
                c = open(f"{path}/script/{selfpath}.js")
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
            
            # Merge all the files together procedrealy
            # todo: make compiler verson of this 
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
            
            # send out html 
            self.wfile.write(content.encode())
        else:
            selfpath = "404"

             # html loading
            try:
                h = open(f"{path}/html/{selfpath}.html")
                ch = h.read()
            except:
                ch = "<h1> 404 not found </h1> <p>ezweb</p>"

            try:
                c = open(f"{path}/html/nav.html")
                nav = c.read()
            except:
                nav=""
                print("no all.css found, skiping")

            #css loading
            
            try:
                c = open(f"{path}/css/{selfpath}.css")
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
                c = open(f"{path}/script/{selfpath}.js")
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



            
            # Merge all the files together procedrealy
            # todo: make compiler verson of this 
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
            print(paths.replace("/",""))
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(content.encode())
            self.end_headers()


# Set the server address and port
server_address = ('', port)

# Create the HTTP server
httpd = HTTPServer(server_address, MyHandler)

# Serve the webpage
print(f"Serving on port {port}")
httpd.serve_forever()
