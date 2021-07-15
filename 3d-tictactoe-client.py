import socket
import argparse
from tictactoe3d import tictactoe3d

ttt = tictactoe3d.tictactoe3d()


parser = argparse.ArgumentParser()
parser.add_argument("--port", help="its the port number", required=True)
parser.add_argument("--ip", help="its the ipaddress")
args = parser.parse_args()

# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# connection to hostname on the port.
clientsocket.connect((args.ip, int(args.port)))

(1, 1, 1)

while True:
    # Receive no more than 1024 bytes
    response = clientsocket.recv(1024).decode("ascii")
    # response will look like this: (layer, row, col)
    response = eval(response)

    ttt.modify_cube(response[0], response[1], response[2])

    print(response)

    inp = ttt.get_input("O")

    clientsocket.send(inp.encode("ascii"))

    if response.rstrip("\n") == "END" or inp.rstrip("\n") == "END":
        print("ending")
        break