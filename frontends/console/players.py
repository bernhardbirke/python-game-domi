# frontends/console/players.py

from library.src.domi.game.players import Player
from library.src.domi.logic.exceptions import InvalidMove
from library.src.domi.logic.models import GameState, Move


class ConsolePlayer(Player):
    def get_move(self, game_state: GameState) -> Move | None:
        while not game_state.game_over:
            try:
                index = grid_to_index(input(f"{self.mark}'s move: ").strip())
            except ValueError:
                print("Please provide coordinates in the form of 1A or A1")
            else:
                try:
                    return game_state.make_move_to(index)
                except InvalidMove:
                    print("That cell is already occupied.")
        return None
