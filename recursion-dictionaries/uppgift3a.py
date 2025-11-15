
def new_board():
    board = {"pieces": {}}
    return board


def is_free(board, x, y):
    try:
        test = board["pieces"][(x, y)]
        return False
    except KeyError:
        return True


def place_piece(board, x, y, player):
    if is_free(board, x, y):
        board["pieces"].update({(x, y): player})
        return True
    else:
        return False


def get_piece(board, x, y):
    if is_free(board, x, y):
        return False
    else:
        piece = board["pieces"][(x, y)]
        return piece


def remove_piece(board, x, y):
    if is_free(board, x, y):
        return False
    else:
        del board["pieces"][(x, y)]
        return True


def move_piece(board, old_x, old_y, new_x, new_y):
    player = board["pieces"][(old_x, old_y)]
    if is_free(board, old_x, old_y) and is_free(board, new_x, new_y):
        return False
    else:
        place_piece(board, new_x, new_y, player)
        remove_piece(board, old_x, old_y)
        return True


def count(board, row_or_column, coordinate, player):
    sum = 0
    if row_or_column == "column":
        for piece in board["pieces"].keys():
            if piece[0] == coordinate:
                sum += 1
    if row_or_column == "row":
        for piece in board["pieces"].keys():
            if piece[1] == coordinate:
                sum += 1
    return sum


def nearest_piece(board, x1, y1):

    smallest_hypotenuse = 1000000

    nearest_piece = False

    for x2, y2 in board["pieces"].keys():
        x_cathetus = abs(x1-x2)
        y_cathetus = abs(y1-y2)
        hypotenuse = (x_cathetus**2 + y_cathetus**2)**0.5

        if hypotenuse < smallest_hypotenuse:
            smallest_hypotenuse = hypotenuse
            nearest_piece = (x2, y2)

    return nearest_piece


if __name__ == "__main__":
    board = new_board()
    print(board)

    assert(is_free(board, 100, 100) == True)

    place_piece(board, 100, 100, "player1")
    place_piece(board, 100, 200, "player2")
    place_piece(board, 10000, 40000, "player3")
    place_piece(board, 200, 100, "player1")
    place_piece(board, 200, 200, "player2")
    place_piece(board, 10100, 40000, "player3")
    print(board)

    print(is_free(board, 100, 100))
    remove_piece(board, 100, 100)
    print(is_free(board, 100, 100))
    print(board)

    move_piece(board, 200, 100, 5677, 4264)
    print(board)

    print(count(board, "row", 40000, "player3"))
    print(count(board, "row", 40001, "player3"))

    print(nearest_piece(board, 300, 300))
    print(nearest_piece(board, 10030, 50000))

    board2 = new_board()
    print(nearest_piece(board2, 0, 0))
