import socket
import argparse
from tictactoe3d import tictactoe3d

ttt = tictactoe3d()


parser = argparse.ArgumentParser()
parser.add_argument("--port", help="its the port number", required=True)
parser.add_argument("--ip", help="its the ipaddress")
args = parser.parse_args()

# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# connection to hostname on the port.
clientsocket.connect((args.ip, int(args.port)))


while True:
    # Receive no more than 1024 bytes
    response = clientsocket.recv(1024).decode("ascii")
    # response will look like this: (layer, row, col)

    response = eval(response)

    ttt.modify_cube(response[0], response[1], response[2], "X")

    ttt.players[0]["score"] = ttt.check_win("X")
    ttt.players[1]["score"] = ttt.check_win("O")

    ttt.draw()

    if ttt.players[0]["score"] >= 3:
        print("X", "wins")
        ttt.draw()
        break

    if ttt.players[1]["score"] >= 3:
        print("O", "wins")
        ttt.draw()
        break

    layer, row, col = ttt.get_input("O")
    ttt.modify_cube(layer, row, col, "O")

    ttt.players[0]["score"] = ttt.check_win("X")
    ttt.players[1]["score"] = ttt.check_win("O")

    ttt.draw()

    if ttt.players[0]["score"] >= 3:
        print("X", "wins")
        ttt.draw()
        break

    if ttt.players[1]["score"] >= 3:
        print("O", "wins")
        ttt.draw()
        break

    clientsocket.send(f"({layer},{row},{col})".encode("ascii"))
