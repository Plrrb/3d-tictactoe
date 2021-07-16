import socket
import argparse
from tictactoe3d import tictactoe3d

ttt = tictactoe3d()

print(ttt.cube)


parser = argparse.ArgumentParser()
parser.add_argument("--port", help="its the port number", required=True)


args = parser.parse_args()
print(args)


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind to the port
print(socket.gethostname())
serversocket.bind((socket.gethostname(), int(args.port)))
serversocket.listen(5)

clientsocket, addr = serversocket.accept()
print("Got a connection from %s" % str(addr))


def main():
    game_over = False

    while not game_over:

        ttt.draw()

        layer, row, col = ttt.get_input("X")

        ttt.modify_cube(layer, row, col, "X")

        ttt.players[1]["score"] = ttt.check_win("O")
        ttt.players[0]["score"] = ttt.check_win("X")

        ttt.draw()

        clientsocket.send(f"({layer},{row},{col})".encode("ascii"))

        if ttt.players[0]["score"] >= 3:
            print("X", "wins")
            ttt.draw()
            break

        if ttt.players[1]["score"] >= 3:
            print(ttt.players[1]["symbol"], "wins")
            ttt.draw()
            break

        response = clientsocket.recv(1024).decode("ascii")

        response = eval(response)

        ttt.modify_cube(response[0], response[1], response[2], "O")

        ttt.players[0]["score"] = ttt.check_win("X")
        ttt.players[1]["score"] = ttt.check_win("O")

        if ttt.players[0]["score"] >= 3:
            print("X", "wins")
            ttt.draw()
            break

        if ttt.players[1]["score"] >= 3:
            print(ttt.players[1]["symbol"], "wins")
            ttt.draw()
            break


main()