# frontends/play.py

from domi.game.engine import Domi
from domi.game.players import RandomComputerPlayer
from domi.logic.models import Mark, Grid, Card

from console.players import ConsolePlayer
from console.renderers import ConsoleRenderer

starting_supply: list[Card] = [
    chapel,
    duchy,
    gold,
    silver,
]
starting_deck: list[Card] = [copper, copper, copper, estate]
starting_grid: Grid = Grid(starting_supply, starting_deck)

player1 = ConsolePlayer(Mark("X"), starting_grid)
player2 = RandomComputerPlayer(Mark("O"), Grid())

Domi(player1, player2, ConsoleRenderer()).play()
