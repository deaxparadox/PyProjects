import json 
import argparse
import subprocess
import unittest
import typing
import socket 
import logging 
import sys 

logging.basicConfig(
    format=("%(asctime)s %(message)s"),
    filemode="a",
    # filename="Socket.log"
)



class Helper:
    @staticmethod
    def Argument():
        args = argparse.ArgumentParser()
        args.add_argument("role", type=str, default="server", help="Describe the role server or client")
        args.add_argument("--host", type=str, default="localhost", help="Host, Default to localhost")
        args.add_argument("--port", type=int, default=13000, help="Port, Default to 13000")
        args.add_argument("-c", type=str, default=None, help="Enter cmd to run")
        return args.parse_args()

    JSONType = typing.AnyStr


class Data:
    # convert given data to bytes
    # or simple it encode the given string
    def to_bytes(self, data: typing.Any = None):
        assert data is not None 
        logging.warning(f"{self.to_bytes.__name__}: Converting data to bytes.")
        return data.encode()

    # decode data to 'utf-8'
    def to_utf8(self, data: bytes = None):
        assert data is not None 
        logging.warning(f"{self.to_utf8.__name__}: Decoding data.")
        return data.decode('utf-8')

    # encode to JSON string
    def ConvertToJSON(self, data: typing.Any = None ) -> Helper.JSONType:
        logging.warning("{}: Converting message to JSON".format(Data.ConvertToJSON.__name__))
        if data is None:
            data = "This is the test string."
        logging.warning("{}: Returning JSON string".format(Data.ConvertToJSON.__name__))
        return json.dumps(data)

    # decode from JSON string
    def RetreiveFromJSON(self, data: bytes = None) -> Helper.JSONType: 
        assert data is not None
        logging.warning(f"{self.RetreiveFromJSON.__name__}: Reverting JSON object.")
        return json.loads(data)

    # for sending over network 
    # 1. encode data to JSON string
    # 2. encode data to bytes 
    def to_send(self, data: typing.AnyStr = None):
        assert data is not None 
        return self.to_bytes(self.ConvertToJSON(data))

    # for received over network
    # 1. decode data 
    # 2. decode JSON string
    def to_receive(self, data: bytes = None):
        assert data is not None 
        return self.RetreiveFromJSON(self.to_utf8(data))





class TCP(Data):
    def __init__(self, host: str = None, port: int = None) -> None:
        self.host = host 
        self.port = port 
        self.address = (self.host, self.port)
        self.ipv4andprotcol = socket.AF_INET, socket.SOCK_STREAM

    
    def run_command(self, *args):
        output = subprocess.run(args, capture_output=True)
        cmd = dict(
            status=output.returncode, 
            stdout=self.to_utf8(output.stdout), 
            stderr=self.to_utf8(output.stderr)
        )
        return cmd


    def server(self):
        sock = socket.socket(*self.ipv4andprotcol)
        logging.warning("{}: Created socket object".format(self.server.__name__))

        sock.bind(self.address)
        logging.warning("{}: Binded to {}".format(self.server.__name__, self.address))

        sock.listen(1)
        logging.warning("{}: Listing...".format(self.server.__name__))

        while True:
            logging.warning("{}: Waiting for client".format(self.server.__name__))
            try:
                connection, client_address = sock.accept()
                logging.warning("{}: Client from {}".format(self.server.__name__, client_address))
            except KeyboardInterrupt:
                logging.warning("{}: Shutting down server...".format(self.server.__name__))
                print()
                sys.exit(1)
            try:
                message = b""
                print("connection from", client_address)
                while True:
                    data = connection.recv(16)
                    if data:
                        message += data
                        # logging.warning("{}: Sending back to the client: ".format(self.server.__name__, {}))
                        connection.sendall(data)
                    else:
                        # logging.warning("{}: No data from {}".format(self.server.__name__, client_address))
                        break
                cmd = self.to_receive(message).get("cmd")
                cmd = self.run_command(*cmd)
                print(cmd.get("status"))
                print(cmd.get("stdout"))
                print(cmd.get("stderr"))
            finally:
                connection.close()

    

    def client(self, message: str = None):
        assert bytes is not None

        sock = socket.socket(*self.ipv4andprotcol)
        print("connecting to {} port {}".format(*self.address))

        sock.connect(self.address)
        logging.warning("{}: Connected to {}".format(self.client.__name__, self.address))

        message = self.to_send(message)

        try:
            print("sending {!r}".format(message))
            sock.sendall(message)
            amount_received = 0 
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = sock.recv(16)
                amount_received += len(data)
                print('received {!r}'.format(data))
        finally:
            print('closing socket')
            sock.close()

        
    @staticmethod
    def main(): 
        Params = Helper.Argument()
        tcp = TCP(Params.host, Params.port)
        
        
        choose = dict(
            server=tcp.server,
            client=tcp.client,
        )
        choice = Params.role
        if choice == "server":
            choose.get(choice)()
        else:
            data = dict(
                cmd=['ls', '-l']
            )
            choose.get(choice)(data)

if __name__ == "__main__":
    TCP.main()