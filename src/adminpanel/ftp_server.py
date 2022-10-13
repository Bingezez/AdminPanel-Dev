import logging

from os.path import abspath
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


class Server:
    def __init__(self, user="user", psw="user_admin", path=".", perm="elradfmwMT") -> None:
        self.user = user
        self.psw = psw
        self.path = abspath(path)
        self.perm = perm
        self._auth = DummyAuthorizer()
        self._handler = FTPHandler

    @staticmethod
    def main():
        connect = Server()
        connect.new_user()
        connect.start_server()


    def new_user(self):
        self._auth.add_user(self.user, self.psw, self.path, self.perm)

        self._handler.authorizer = self._auth
    
    def start_server(self, host='127.0.0.1', port=5050):
        server = FTPServer((host, port), self._handler)
        server.serve_forever()


if __name__ == '__main__':
    test = Server()
    test.main()
