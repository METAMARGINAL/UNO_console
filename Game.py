# Game.py
from Deck import generate_full_deck
from Player import Player

class Game:
    def __init__(self):
        self.deck = generate_full_deck()
        self.players = []
        self.top_card = None
        self.current_player_idx = 0
        self.direction = 1  # 1 = по часовой, -1 = против часовой

    def add_player(self, player: Player):
        self.players.append(player)

    def current_player(self):
        return self.players[self.current_player_idx]

    def draw_cards(self, player: Player, count: int):
        for _ in range(count):
            if self.deck:
                player.draw_card(self.deck.pop())
            else:
                print("Колода пуста!")

    def clear_console(self):
        print("\033[H\033[J", end="")

    def start(self):
        # Раздаём карты игрокам
        for player in self.players:
            for _ in range(7):
                player.draw_card(self.deck.pop())

        # Первая карта на столе должна быть обычной
        import random
        while True:
            card = self.deck.pop()
            if not card.isSpecial:
                self.top_card = card
                break
            else:
                self.deck.insert(0, card)
                random.shuffle(self.deck)

        print(f"Первая карта на столе: {self.top_card}")

        # Игровой цикл
        while True:
            self.play_turn()
            # Проверка на победителя
            for player in self.players:
                if not player.hand:
                    print(f"\n{player.name} выиграл игру! Поздравляем!")
                    exit()

    def play_turn(self):
        self.clear_console()
        player = self.current_player()
        print(f"\nХод игрока {player.name}")
        print(f"Текущая карта на столе: {self.top_card}")
        print(f"Ваша рука: {player.show_hand()}")

        while True:
            choice = input("Введите номер карты для игры или 'd' чтобы взять карту: ").strip()
            if choice.lower() == 'd':
                if self.deck:
                    player.draw_card(self.deck.pop())
                    print("Вы взяли карту.")
                else:
                    print("Колода пуста!")

                # Переход хода следующему игроку
                self.current_player_idx = (self.current_player_idx + self.direction) % len(self.players)
                break

            elif choice.isdigit():
                index = int(choice)
                if index < 0 or index >= len(player.hand):
                    print("Некорректный номер карты.")
                    continue
                card = player.hand[index]
                if card.isPlayableOn(self.top_card):
                    player.play_card(index, self)
                    # Для обычной карты или Wild (без спецэффекта) ход переходит следующему
                    if not card.isSpecial or card.denomination == "wild":
                        self.current_player_idx = (self.current_player_idx + self.direction) % len(self.players)
                    break
                else:
                    print("Эту карту нельзя сыграть. Выберите другую.")
            else:
                print("Некорректный ввод.")
