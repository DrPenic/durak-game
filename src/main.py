from cards import *
from game import *
from ai import *

deck = create_deck()
shuffle_deck(deck)
trump_card, trump_suit = get_trump(deck)
player_hand, computer_hand, deck = deal_cards(deck)

attacker = 'player'

while player_hand is not None and computer_hand is not None:
    print('\n==========')
    print(f'Козырь: {trump_suit}')

    if attacker == 'player':
        print('Твой ход: ')
        success = turn(player_hand, computer_hand, 'human', 'ai', trump_suit, table)
        attacker = 'computer' if success else 'player'
    else:
        print('Ход противника: ')
        success = turn(computer_hand, player_hand, 'ai', 'human', trump_suit, table)
        attacker = 'player' if success else 'computer'
    if success:
        table.clear()
    draw_cards(player_hand, computer_hand, deck)
    if len(deck) == 0 and not player_hand:
        print('Ты выиграл!')
        break
    elif len(deck) == 0 and not computer_hand:
        print('Ты проиграл!')
        break

    print('\n--- Состояние ---')
    print('Ты: ', len(player_hand), 'карт')
    print('Комп: ', len(computer_hand), 'карт')

    input('\nEnter для следующего хода...')
