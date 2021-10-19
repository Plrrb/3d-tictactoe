# 3d-tictactoe

A 3D tic tac toe game made in Python,\
in 3D tic tac toe there are 3 boards in the terminal,\
each board on screen is a layer on a 3D cube in this order \[back\] \[middle\] \[front\]\
first choose a layer 1 to 3\
then choose a place 1 to 9

the first player to 3 tic tac toe's wins

# How to play over the internet

Run the 3d-tictactoe-server.py on one computer

```
python3 3d-tictactoe-server.py --port \<port\>
```

run the 3d-tictactoe-client.py on another computer

```
python3 3d-tictactoe-client.py --port \<port\> --ip \<servers ip\>
```

# how to play locally

```
python3 tictactoe3d.py
```
