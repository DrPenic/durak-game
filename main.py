from cards import *
from game import *
from ai import *

deck = create_deck()
shuffle_deck(deck)
trump_card, trump_suit = get_trump(deck)
player_hand, computer_hand, deck = deal_cards(deck)

attacker = 'player'

while player_hand and computer_hand:
    print('\n==========')
    print(f'Козырь: {trump_suit}')

    if attacker == 'player':
        success = player_attack_turn(player_hand, computer_hand, trump_suit)
        if success:
            attacker = 'computer'
        else:
            attacker = 'player'
    else:
        success = ai_attack_turn(computer_hand, player_hand, trump_suit)
        if success:
            attacker = 'player'
        else:
            attacker = 'computer'

    draw_cards(player_hand, computer_hand, deck)

    print('\n--- Состояние ---')
    print('Ты: ', len(player_hand), 'карт')
    print('Комп: ', len(computer_hand), 'карт')

    input('\nEnter для следующего хода...')

if not player_hand:
    print('Ты выиграл!')
elif not computer_hand:
    print('Компьютер выиграл!')