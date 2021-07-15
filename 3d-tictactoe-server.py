import socket
import argparse
from tictactoe3d import tictactoe3d

ttt = tictactoe3d()

print(ttt.cube)


parser = argparse.ArgumentParser()
parser.add_argument("--port", help="its the port number", required=True)
parser.add_argument("--ip", help="its the ipaddress")

args = parser.parse_args()
print(args)


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind to the port
serversocket.bind((socket.gethostname(), int(args.port)))
serversocket.listen(5)

clientsocket, addr = serversocket.accept()
print("Got a connection from %s" % str(addr))


def main():
    game_over = False

    while not game_over:
        for player in ttt.players:

            ttt.draw()

            ttt.get_input(player["symbol"])

            player["score"] = ttt.check_win(player["symbol"])

            if player["score"] >= 3:
                print(player["symbol"], "wins")
                ttt.draw()
                game_over = True
                break


main()