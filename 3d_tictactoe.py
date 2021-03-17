empty = " "

cube = [
    [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ],
    [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ],
    [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ],
]


def draw():
    for row in range(3):
        for layer in cube:
            print(
                f" {layer[row][0]} | {layer[row][1]} | {layer[row][2]} ", end=" ")
        print("")
        if row != 2:
            print("---|---|--- ---|---|--- ---|---|---")


def is_layer_full(layer):
    for row in cube[layer]:
        for elt in row:
            if elt == empty:
                return False
    return True


def input_to_int(text):
    while True:
        inp = input(text)
        try:
            inp = int(inp)
            break
        except:
            print("not a number")

    return inp


def get_input(player):
    # get input for layer
    while True:
        layer = input_to_int(player + " choose a layer: ") - 1
        if layer >= 3 or layer < 0:
            print("number out of bounds")
            continue

        if not is_layer_full(layer):
            break
        else:
            print("that layer is full")

    # get input for place
    while True:
        place = input_to_int(player + " choose a place: ") - 1
        if not 0 <= place <= 9:
            print("number out of bounds")
            continue

        row = place // 3
        index = place % 3

        if cube[layer][row][index] == empty:
            cube[layer][row][index] = player
            break
        else:
            print("that place is taken")


def check_win(player):
    # all in a row
    for layer in cube:
        for row in layer:
            if player == row[0] == row[1] == row[2]:
                return True

    # all in a column
    for layer in cube:
        for col in range(3):
            if player == layer[0][col] == layer[1][col] == layer[2][col]:
                return True

    # split layer all in row
    for i in range(3):
        for j in range(3):
            if player == cube[0][i][j] == cube[1][i][j] == cube[2][i][j]:
                return True

    # one layer diagonal
    for layer in cube:
        if (
            player == layer[0][0] == layer[1][1] == layer[2][2]
            or player == layer[0][2] == layer[1][1] == layer[2][0]
        ):
            return True

    # multi layer diagonal
    for i in range(3):
        if (
            player == cube[0][0][i] == cube[1][1][i] == cube[2][2][i]
            or player == cube[0][2][i] == cube[1][1][i] == cube[2][0][i]
        ):
            return True

    # horizontal diagonal
    for i in range(3):
        if (
            player == cube[0][i][0] == cube[1][i][1] == cube[2][i][2]
            or player == cube[2][i][0] == cube[1][i][1] == cube[0][i][2]
        ):
            return True

    # thru opposite corners of the cube
    # top left
    if (player == cube[0][0][0] == cube[1][1][1] == cube[2][2][2] or
            # top right
            player == cube[0][0][2] == cube[1][1][1] == cube[2][2][0] or
            # bottom left
            player == cube[0][2][0] == cube[1][1][1] == cube[2][0][2] or
            # bottom right
            player == cube[0][2][2] == cube[1][1][1] == cube[2][0][0]):
        return True

x_score = 0
o_score = 0
while True:
    draw()
    get_input("X")

    if check_win("X"):
        print("X wins")
        draw()
        break

    draw()
    get_input("O")

    if check_win("O"):
        print("O wins")
        draw()
        break

#  X | O | X
# ---|---|---
#  X | X | X
# ---|---|---
#  O | X | O
