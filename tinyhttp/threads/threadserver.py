from __future__ import absolute_import
from threading import Thread, current_thread

from ..http.server import HttpServer
from ..helpers import Signal, argv


class ThreadHttpServer(HttpServer):
    
    def _run(self):
        self.sock.listen(self.backlog)
        while True:
            sock, addr = self.sock.accept()
            if Signal.debug:
                    print("Connect by {} Port {}".format(*addr))
            Thread(target=self._echo, args=(sock,)).start()


def main():
    port = 8888
    if len(argv) > 1:
        port = int(argv[1])
    serv = HttpServer(port=port)
    try:
        serv()
    except KeyboardInterrupt:
        Signal.go = False
        print("  Good bye", flush=True)