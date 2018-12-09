#!/usr/bin/env python

import re

from git import Repo
from xo.board import Board
from xo.game import Game

place_x = re.compile(' *[xX] *(\\||$)')
place_o = re.compile(' *[oO] *(\\||$)')
empty = re.compile(' +(\\||$)')
padding = re.compile('[^\\.xo]*')

def load_board(game_in):
    board_data = ''
    for line in game_in.decode('ascii').split('\n'):
        line = place_x.sub('x', line)
        line = place_o.sub('o', line)
        line = empty.sub('.', line)
        line = padding.sub('', line)
        board_data += line.strip()
    return Board.fromstring(board_data)


if __name__ == '__main__':
    # Load board states from current and previous commits:
    r = Repo()
    last_board = load_board((r.commit('HEAD~1').tree / 'game.txt').data_stream.read())
    cur_board = load_board((r.head.commit.tree / 'game.txt').data_stream.read())

    # Reload game from last board:
    g = Game()
    g.start('x')
    g.board = last_board

    # Find the move:
    for i, p in enumerate(cur_board.cells):
        if last_board.cells[i] != p:
            col = i % 3
            row = int((i - col) / 3)
            e = g.moveto(row+1, col+1)
            print(e)

    print(cur_board.toascii())
    print(last_board.toascii())
