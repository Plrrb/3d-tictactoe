class tictactoe3d:
    def __init__(self):

        self.empty = " "

        self.cube = [
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

        self.players = [
            {"symbol": "X", "score": 0},
            {"symbol": "O", "score": 0},
        ]

    def draw(self):
        for row in range(3):
            for layer in self.cube:
                print(f" {layer[row][0]} | {layer[row][1]} | {layer[row][2]} ", end=" ")
            print("")
            if row != 2:
                print("---|---|--- ---|---|--- ---|---|---")

        for player in self.players:
            print(player["symbol"], "Score:", player["score"])

    def is_layer_full(self, layer):
        for row in self.cube[layer]:
            for elt in row:
                if elt == self.empty:
                    return False
        return True

    def input_to_int(self, text):
        while True:
            inp = input(text)
            try:
                inp = int(inp)
                break
            except:
                print("not a number")

        return inp

    def get_input(self, player):
        # get input for layer
        while True:
            layer = self.input_to_int(player + " choose a layer: ") - 1
            if layer >= 3 or layer < 0:
                print("number out of bounds")
                continue

            if self.is_layer_full(layer):
                print("that layer is full")
                continue

            # get input for place
            place = self.input_to_int(player + " choose a place: ") - 1
            if place >= 9 or place < 0:
                print("number out of bounds")
                continue

            row = place // 3
            index = place % 3

            if self.cube[layer][row][index] == self.empty:
                return layer, row, index
            print("that place is taken")

    def modify_cube(self, layer, row, col, player):
        self.cube[layer][row][col] = player

    def check_win(self, player):
        wins = 0

        # all in a row
        for layer in self.cube:
            for row in layer:
                if player == row[0] == row[1] == row[2]:
                    wins += 1

        # all in a column
        for layer in self.cube:
            for col in range(3):
                if player == layer[0][col] == layer[1][col] == layer[2][col]:
                    wins += 1

        # split layer all in row
        for i in range(3):
            for j in range(3):
                if (
                    player
                    == self.cube[0][i][j]
                    == self.cube[1][i][j]
                    == self.cube[2][i][j]
                ):
                    wins += 1

        # one layer diagonal
        for layer in self.cube:
            wins += player == layer[0][0] == layer[1][1] == layer[2][2]
            wins += player == layer[0][2] == layer[1][1] == layer[2][0]

        # multi layer diagonal
        for i in range(3):
            wins += (
                player == self.cube[0][0][i] == self.cube[1][1][i] == self.cube[2][2][i]
            )
            wins += (
                player == self.cube[0][2][i] == self.cube[1][1][i] == self.cube[2][0][i]
            )

        # horizontal diagonal
        for i in range(3):
            wins += (
                player == self.cube[0][i][0] == self.cube[1][i][1] == self.cube[2][i][2]
            )
            wins += (
                player == self.cube[2][i][0] == self.cube[1][i][1] == self.cube[0][i][2]
            )

        # thru opposite corners of the self.cube
        # top left
        wins += player == self.cube[0][0][0] == self.cube[1][1][1] == self.cube[2][2][2]
        # top right
        wins += player == self.cube[0][0][2] == self.cube[1][1][1] == self.cube[2][2][0]
        # bottom left
        wins += player == self.cube[0][2][0] == self.cube[1][1][1] == self.cube[2][0][2]
        # bottom right
        wins += player == self.cube[0][2][2] == self.cube[1][1][1] == self.cube[2][0][0]

        return wins


# def main():
#     game_over = False

#     while not game_over:
#         for player in players:

#             draw()

#             get_input(player["symbol"])

#             player["score"] = check_win(player["symbol"])

#             if player["score"] >= 3:
#                 print(player["symbol"], "wins")
#                 draw()
#                 game_over = True
#                 break


# if __name__ == "__main__":
# main()
