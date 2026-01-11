from src.player import Player
from src.board import Board
from src.game import Game
import random
import time


def main():
    p1 = Player(is_computer=False)
    p2 = Player(is_computer=True)
    b1 = Board()
    g1 = Game(p1, p2, b1)
    g1.start_game()
    g1.start_rounds()


if __name__ == "__main__":
    main()
