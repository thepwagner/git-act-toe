#!/usr/bin/env python

from git import Repo
from gat.game import PersistentGame


if __name__ == '__main__':
    # Load game file from commit:
    r = Repo('..')
    game_data = (r.head.commit.tree / 'game.txt').data_stream.read().decode('utf-8').split('\n')

    # First line is signed game state:
    game = PersistentGame.fromstring(game_data[0])

    game_data[]

    print(game.render())
