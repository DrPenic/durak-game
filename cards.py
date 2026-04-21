import random

def create_deck():
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    deck = [(rank, suit) for suit in suits for rank in ranks]
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def get_trump(deck):
    trump_card = deck[-1]
    trump_suit = trump_card[1]
    return trump_card, trump_suit

def deal_cards(deck, num_cards = 6):
    player_hand = []
    computer_hand = []
    for _ in range(num_cards):
        player_hand.append(deck.pop(0))
        computer_hand.append(deck.pop(0))
    return player_hand, computer_hand, deck

def card_value(rank):
    order = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return order.index(rank)

def card_strength(card, trump_suit):
    rank, suit = card
    base = card_value(rank)

    if suit == trump_suit:
        base += 100
    return base
