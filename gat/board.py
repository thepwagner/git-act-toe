import re
from xo.board import Board

place_x = re.compile(' *[xX] *(\\||$)')
place_o = re.compile(' *[oO] *(\\||$)')
empty = re.compile(' +(\\||$)')
padding = re.compile('[^\\.xo]*')


def load_board(game_in):
    board_data = ''
    for line in game_in:
        line = place_x.sub('x', line)
        line = place_o.sub('o', line)
        line = empty.sub('.', line)
        line = padding.sub('', line)
        board_data += line.strip()
    return Board.fromstring(board_data)
