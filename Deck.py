# Deck.py
from Card import Card, SkipCard, ReverseCard, DrawTwoCard, WildCard, DrawFourCard
import random

def generate_full_deck():
    colors = ["red", "blue", "green", "yellow"]
    deck = []

    for color in colors:
        deck.append(Card(color, "0"))
        for num in range(1, 10):
            deck.append(Card(color, str(num)))
            deck.append(Card(color, str(num)))
        for _ in range(2):
            deck.append(SkipCard(color))
            deck.append(ReverseCard(color))
            deck.append(DrawTwoCard(color))

    for _ in range(4):
        deck.append(WildCard())
        deck.append(DrawFourCard())

    random.shuffle(deck)
    return deck
