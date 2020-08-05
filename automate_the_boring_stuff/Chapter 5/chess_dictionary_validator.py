import re

board1 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '7e': 'bpawn', '1e': 'bpawn',
          '5b': 'bpawn'}

board2 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '7e': 'bpawn', '1e': 'bpawn',
          '13b': 'bpawn'}


def is_valid_board(board):
    print(f'Validating {board}: ')
    if check_kings(board):
        print('valid kings, checking next')
    else:
        print('invalid king count')
        return False
    if check_pawns(board):
        print('valid pawns, checking next')
    else:
        return False
    if check_coordinates(board):
        print('valid coordinates')
    else:
        print('INVALID COORDINATES')
        return False
    return True


def check_kings(board):
    bking = sum(1 for piece in board.values() if piece == 'bking')
    wking = sum(1 for piece in board.values() if piece == 'wking')
    if bking == 1 and wking == 1:
        return True
    else:
        return False


def check_coordinates(board):
    for key in board.keys():
        if not re.match('[0-8][a-h]', key):
            return False
    return True


def check_pawns(board):
    bpawns = sum(1 for piece in board.values() if piece == 'bpawn')
    wpawns = sum(1 for piece in board.values() if piece == 'wpawn')
    if bpawns not in range(0, 9) or wpawns not in range(0, 9):
        return False
    else:
        return True


print(is_valid_board(board1))
print(is_valid_board(board2))
