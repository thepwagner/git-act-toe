import base64
import hashlib
import hmac
import json
import uuid

from xo.board import Board
from xo.game import Game

# TODO: load from environment
key = 'SECRET_FROM_ENVIRONMENT'.encode('utf-8')


class PersistentGame(object):
    def __init__(self, game=None, game_id=None):
        if game:
            self.game = game
        else:
            self.game = Game()
            self.game.start('x')
        self.id = game_id or str(uuid.uuid4())

    def save(self):
        state = {
            'id': self.id,
            'board': self._board(),
            'turn': self.game.turn
        }
        signature = hmac.new(key, json.dumps(state, sort_keys=True).encode('utf-8'), hashlib.sha512).digest()
        state['signature'] = base64.standard_b64encode(signature).decode('utf-8')
        return json.dumps(state, sort_keys=True)

    def render(self):
        return '{}\n\n```\n{}\n```\n'.format(self.save(), self.game.board.toascii())

    def _board(self):
        b = ''
        for c in self.game.board.cells:
            if c == ' ':
                b += '.'
            elif c == 'x' or c == 'y':
                b += c
        return b

    @classmethod
    def fromstring(cls, string):
        state = json.loads(string)

        # Verify signature:
        signature = state['signature']
        del state['signature']
        calculated = hmac.new(key, json.dumps(state, sort_keys=True).encode('utf-8'), hashlib.sha512).digest()
        if base64.standard_b64encode(calculated).decode('utf-8') != signature:
            raise Exception('signature mismatch')

        # Rebuild game from verified state:
        g = Game()
        g.start('x')
        g.board = Board.fromstring(state['board'])
        g.turn = state['turn']
        return PersistentGame(g, state['id'])
