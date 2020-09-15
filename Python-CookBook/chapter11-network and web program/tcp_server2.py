# -*- coding: utf-8 -*-
# github: https://github.com/houm01

from socketserver import StreamRequestHandler, TCPServer


class EchoHandler(StreamRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)

        for line in self.rfile:
            self.wfile.write(line)


if __name__ == '__main__':
    # serv = ThreadingTCPServer(('', 20000), EchoHandler)
    # serv.serve_forever()
    from threading import Thread
    NWORKERS = 16
    serv = TCPServer(('', 20000), EchoHandler, bind_and_activate=False)
    for n in range(NWORKERS):
        t = Thread(target=serv.serve_forever)
        t.daemon = True
        t.start()
    serv.serve_forever()