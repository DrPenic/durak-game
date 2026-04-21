from cards import card_strength, card_value

def ai_attack(hand, trump_suit):
    return min(hand, key=lambda c: card_strength(c, trump_suit))

def ai_defence(card_to_beat, hand, trump_suit):
    possible = []

    for card in hand:
        if (card[1] == card_to_beat[1] and card_value(card[0]) > card_value(card_to_beat[0]))\
        or (card[1] == trump_suit and card_to_beat[1] != trump_suit):
            possible.append(card)

    if possible:
        return min(possible, key = lambda c: card_strength(c, trump_suit))
    return None