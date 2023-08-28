# domi/game/cards.py

from dataclasses import dataclass

from library.src.domi.logic.models import Card


@dataclass
class Village(Card):
    def play(self):
        print("play village")
        pass


class Smithy(Card):
    def play(self):
        print(f"play {super().name}")
        pass


@dataclass
class Estate(Card):
    def play(self):
        pass


@dataclass
class Copper(Card):
    def play(self):
        pass
