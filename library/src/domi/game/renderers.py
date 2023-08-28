# domi/game/renderers.py

import abc

from domi.logic.models import GameState


class Renderer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def render(self, game_state: GameState) -> None:
        """render the current game state"""
