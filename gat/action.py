#!/usr/bin/env python3

import sys

from git import Repo
from gat.board import load_board
from gat.game import PersistentGame
from xo.game import EVENT_NAME_NEXT_TURN, STATE_GAMEOVER


if __name__ == '__main__':
    # Load game file from commit:
    r = Repo('..')
    game_data = (r.head.commit.tree / 'game.txt').data_stream.read().decode('utf-8').split('\n')

    # First line is signed game state:
    game = PersistentGame.fromstring(game_data[0])

    # Remaining lines are the updated game board:
    new_board = load_board(game_data[1:])

    # Find the cell that changed:
    for i, p in enumerate(game.game.board.cells):
        if new_board.cells[i] != p:
            col = i % 3
            row = int((i - col) / 3)
            e = game.game.moveto(row+1, col+1)
            print(e)
            if e['name'] == EVENT_NAME_NEXT_TURN:
                print(game.render())
                # TODO: commit and push this new state
            elif game.game.state == STATE_GAMEOVER:
                sys.exit(1)
