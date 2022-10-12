from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_POST(self):
        print("POST request")
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        print("Headers:", self.headers)
        print("Data:", post_data.decode("utf-8"))
        self._set_response()


def run():
    httpd = HTTPServer(("", 8080), Handler)
    print(httpd)
    httpd.serve_forever()
    httpd.server_close()


if __name__ == "__main__":
    run()
