# Player.py
from Card import Card

class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []

    def draw_card(self, card: Card):
        self.hand.append(card)

    def play_card(self, index: int, game_state) -> bool:
        if index < 0 or index >= len(self.hand):
            return False
        card = self.hand.pop(index)
        if card.isSpecial:
            card.special_action(game_state)
        game_state.top_card = card
        return True

    def show_hand(self):
        hand_str = []
        for i, card in enumerate(self.hand):
            hand_str.append(f"{i}: {card}")
        return ", ".join(hand_str)
