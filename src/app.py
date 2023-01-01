from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl, requests, json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def get_data(self):
        myrequest = requests.get(
            "https://www.hebcal.com/hebcal?v=1&cfg=json&maj=on&min=on&mod=on&nx=on&start=2021-03-01&end=2021-06-31&ss=on&mf=on&c=on&geo=geoname&geonameid=281184&M=on&s=on")
        json_str = myrequest.text
        data = json.loads(json_str)
        json_tmp = []
        for item in data['items']:
            title = item['title']
            date = item['date']
            json_tmp.append({"Holiday": title, "Date": date})
        
        json_object = json.dumps(json_tmp, indent=4)
        print(json_object) 
        return json_object

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        ret = self.get_data()
        self.wfile.write(ret.encode(encoding='utf_8'))
    
    
try:
    httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)


    
    #httpd.socket = ssl.wrap_socket(httpd.socket,
    #                               keyfile="key.pem",
    #                               certfile='cert.pem', server_side=True)
    print('Starting the web server...')
    httpd.serve_forever()


except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    httpd.socket.close()

