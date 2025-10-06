# Card.py
import random

COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "reset": "\033[0m"
}

class Card:
    def __init__(self, color: str, denomination: str):
        self.color = color
        self.denomination = denomination
        self.isSpecial = False

    def isPlayableOn(self, other_card):
        return self.color == other_card.color or self.denomination == other_card.denomination or self.color is None

    def __str__(self):
        color_code = COLORS.get(self.color, "")
        reset_code = COLORS["reset"]
        if self.color:
            return f"{color_code}{self.color} {self.denomination}{reset_code}"
        else:
            return f"{self.denomination}"


class SkipCard(Card):
    def __init__(self, color: str):
        super().__init__(color, "skip")
        self.isSpecial = True

    def special_action(self, game_state):
        next_idx = (game_state.current_player_idx + game_state.direction) % len(game_state.players)
        skipped_player = game_state.players[next_idx]
        print(f"{skipped_player.name} пропускает ход!")
        game_state.current_player_idx = (next_idx + game_state.direction) % len(game_state.players)


class ReverseCard(Card):
    def __init__(self, color: str):
        super().__init__(color, "reverse")
        self.isSpecial = True

    def special_action(self, game_state):
        game_state.direction *= -1
        print("Направление хода изменено!")
        if len(game_state.players) == 2:
            # Для 2 игроков reverse = skip
            game_state.current_player_idx = (game_state.current_player_idx + game_state.direction) % len(game_state.players)
        else:
            game_state.current_player_idx = (game_state.current_player_idx + game_state.direction) % len(game_state.players)


class DrawTwoCard(Card):
    def __init__(self, color: str):
        super().__init__(color, "+2")
        self.isSpecial = True

    def special_action(self, game_state):
        next_idx = (game_state.current_player_idx + game_state.direction) % len(game_state.players)
        game_state.draw_cards(game_state.players[next_idx], 2)
        print(f"{game_state.players[next_idx].name} берёт 2 карты")
        game_state.current_player_idx = (next_idx + game_state.direction) % len(game_state.players)


class WildCard(Card):
    def __init__(self):
        super().__init__(None, "wild")
        self.isSpecial = True

    def special_action(self, game_state):
        chosen_color = input("Выберите цвет (red, blue, green, yellow): ").strip().lower()
        self.color = chosen_color
        print(f"Цвет карты изменён на {self.color}")


class DrawFourCard(Card):
    def __init__(self):
        super().__init__(None, "+4")
        self.isSpecial = True

    def special_action(self, game_state):
        chosen_color = input("Выберите цвет (red, blue, green, yellow): ").strip().lower()
        self.color = chosen_color
        print(f"Цвет карты изменён на {self.color}")

        next_idx = (game_state.current_player_idx + game_state.direction) % len(game_state.players)
        game_state.draw_cards(game_state.players[next_idx], 4)
        print(f"{game_state.players[next_idx].name} берёт 4 карты")
        game_state.current_player_idx = (next_idx + game_state.direction) % len(game_state.players)
