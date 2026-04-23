from cards import card_strength, card_value, can_beat

def ai_attack(hand, trump_suit):
    return min(hand, key=lambda c: card_strength(c, trump_suit))

def ai_defense(attacker_card, hand, trump_suit):
    valid = [c for c in hand if can_beat(c, attacker_card, trump_suit)]
    if not valid:
        return None
    return min(valid, key=lambda c: card_strength(c, trump_suit))