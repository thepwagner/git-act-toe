#!/usr/bin/env python

import re
from xo.board import Board

place_x = re.compile(' *[xX] *(\\||$)')
place_o = re.compile(' *[oO] *(\\||$)')
empty = re.compile(' +(\\||$)')
padding = re.compile('[^\\.xo]*')

def load_board(fn):
    with open('game.txt') as game_txt:
        board_data = ''
        line = game_txt.readline()
        while line:
            line = place_x.sub('x', line)
            line = place_o.sub('o', line)
            line = empty.sub('.', line)
            line = padding.sub('', line)
            board_data += line.strip()
            line = game_txt.readline()
        return Board.fromstring(board_data)

if __name__ == '__main__':
   b = load_board('game.txt')
   print(b.toascii())
