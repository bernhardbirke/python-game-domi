# domi/logic/models.py

import abc
import enum
import random
import re
from dataclasses import dataclass, field
from functools import cached_property
from collections import UserList


@dataclass
class Card:
    name: str
    cost: int
    type: str  # action, victory, treasure, curse
    type2: str | None = None  # attack, reaction

    @property
    def src(self):
        return f"{self.name}.jpg"  # img src

    # @abc.abstractmethod
    def play_card_super(self):
        pass


@dataclass
class Deck(UserList):
    data: list[Card] = field(default_factory=list)  # data = lists of cards


@dataclass
class Grid:
    supply: Deck  # same for all players (sync after every turn)
    deck: Deck
    discard_pile: Deck = field(default_factory=Deck)
    hand: Deck = field(default_factory=Deck)
    cards_played: Deck = field(default_factory=Deck)
    choose_area: Deck = field(
        default_factory=Deck
    )  # special Deck to choose cards from. generally empty after every turn
    trash: Deck = field(default_factory=Deck)  # same for all players


@dataclass
class Stats:
    actions: int = field(default=1)
    buys: int = field(default=1)
    victorypoints: int = field(default=0)
    turns: int = field(default=0)
    money_played: bool = field(default=False)


@dataclass
class GameState:  # TD stack for the game.
    pass


@dataclass(frozen=True)
class Move:
    # mark: Mark
    cell_index: int
    before_state: "GameState"
    after_state: "GameState"
