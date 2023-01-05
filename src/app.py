import http
from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl, requests, json
import pandas as pd


def get_start_end_q():
    now = pd.Timestamp.now()
    current_period = now.to_period('Q')
    next_quarter_period = current_period + 1
    return next_quarter_period.start_time.date().__str__(), next_quarter_period.end_time.date().__str__()


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def get_data(self):
        start_q, end_q = get_start_end_q()
        myrequest = requests.get(
            f"https://www.hebcal.com/hebcal"
            f"?v=1&cfg=json&maj=on&min=on&mod=on&nx=on&"
            f"start={start_q}&end={end_q}&ss=on&mf=on&c=on&"
            f"geo=geoname&geonameid=281184&M=on&s=on")
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

    httpd.serve_forever()
    print(get_start_end_q())

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    httpd.socket.close()
