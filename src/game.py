from ai import ai_attack, ai_defence
from cards import card_value

def show_player_hand(hand):
    print("\nТвои карты:")
    for i, card in enumerate(hand):
        print(f"{i}: {card[0]}{card[1]}")

def ai_attack_turn(computer_hand, player_hand, trump_suit):
    attack_card = ai_attack(computer_hand, trump_suit)
    computer_hand.remove(attack_card)
    
    print(f'Компьютер ходит: {attack_card[0]}{attack_card[1]}')

    show_player_hand(player_hand)
    choice = int(input('Чем отбиться? (-1 - взять): '))

    if choice == -1:
        print('Ты берешь карту')
        player_hand.append(attack_card)
        return False
    
    player_card = player_hand.pop(choice)

    if can_beat(player_card, attack_card, trump_suit):
        print(f'Ты отбился: {player_card[0]}{player_card[1]}')
        return True
    else:
        print('Нельзя так отбиться, ты забираешь карты')
        player_hand.append(player_card)
        player_hand.append(attack_card)
        return False
    
def can_beat(defend, attack, trump_suit):
    if defend[1] == attack[1] and card_value(defend[0]) > card_value(attack[0]):
        return True
    if defend[1] == trump_suit and attack[1] != trump_suit:
        return True
    return False

def player_attack_turn(player_hand, computer_hand, trump_suit):
    show_player_hand(player_hand)

    choice = int(input('\nВыбери карту для атаки: '))
    attack_card = player_hand.pop(choice)

    print(f'\nТвой выбор: {attack_card[0]}{attack_card[1]}')

    defend_card = ai_defence(attack_card, computer_hand, trump_suit)

    if defend_card:
        computer_hand.remove(defend_card)
        print(f'Компьютер отбился: {defend_card[0]}{defend_card[1]}')
        return True
    else:
        print("Компьютер не смог отбиться!")
        computer_hand.append(attack_card)
        return False

def draw_cards(player_hand, computer_hand, deck, attacker_first=True):
    while len(player_hand) < 6 and deck:
        player_hand.append(deck.pop(0))
    while len(computer_hand) < 6 and deck:
        computer_hand.append(deck.pop(0))