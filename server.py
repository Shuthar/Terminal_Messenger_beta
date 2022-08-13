import socketserver
import json

user_names = []
messagers = {}

class ThreadingTSPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class MyTSPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).strip()

        resp = json.loads(data.decode())
        respons_text = ""

        if resp.get("user_name") is not None:
            user_names.append(resp.get("user_name"))
        if resp.get("get") is not None:
            respons_text = messagers.pop(resp.get("get"), "")
        if resp.get("for") is not None:
            messagers.update([(resp.get("for"), resp.get("text"))])

        if respons_text != "":
            print(respons_text)

        self.request.sendall(bytes(respons_text, 'utf-8'))

with ThreadingTSPServer(("127.0.0.1", 1500), MyTSPHandler) as server:
    server.serve_forever()

