# domi/game/players.py

import abc
import time

from library.src.domi.logic.exceptions import InvalidMove
from library.src.domi.logic.models import GameState, Mark, Move, Grid, Stats


class Player(metaclass=abc.ABCMeta):
    def __init__(self, name: str, grid: Grid, stats: Stats) -> None:
        self.name = name
        self.grid = grid
        self.stats = stats

    def make_move(self, game_state: GameState) -> GameState:
        if self.mark is game_state.current_mark:
            if move := self.get_move(game_state):
                return move.after_state
            raise InvalidMove("No more possible moves")
        else:
            raise InvalidMove("It's the other players turn")

    @abc.abstractmethod
    def get_move(self, game_state: GameState) -> Move | None:
        """Return the current player's move in the given game state."""
