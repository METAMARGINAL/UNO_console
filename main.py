# main.py
from Game import Game
from Player import Player

def main():
    game = Game()
    num_players = int(input("Сколько игроков (2-4)? "))
    for i in range(num_players):
        name = input(f"Имя игрока {i+1}: ")
        game.add_player(Player(name))

    game.start()

if __name__ == "__main__":
    main()
