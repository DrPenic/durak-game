from ai import ai_attack, ai_defense
from cards import card_value, can_beat

table = []

def add_attack(table, card):
    table.append({'attack': card, 'defense': None})

def add_defense(table, card):
    for pair in reversed(table):
        if pair['defense'] is None:
            pair['defense'] = card
            return True
    return False

def show_table(table):
    print('\n---Стол---')
    for pair in table:
        if pair["defense"] is not None:
            print(f"{pair['attack'][0]}{pair['attack'][1]} → {pair['defense'][0]}{pair['defense'][1]}")
        else:
            print(f"{pair['attack'][0]}{pair['attack'][1]} → (no defense)")

def show_player_hand(hand):
    print("\nТвои карты:")
    for i, card in enumerate(hand):
        print(f"{i}: {card[0]}{card[1]}")

def valid_choice(prompt, min_val, max_val):
    while True:
        try:
            value = input(prompt).strip()
            if value.lower() == 'q':
                print('Выход из игры')
                exit()
            choice = int(value)
            if min_val <= choice <= max_val:
                return choice
            print(f"Введите число от {min_val} до {max_val}")
        except ValueError:
            print('Введите число, а не текст')

def choose_attack(hand, trump_suit, attacker):
    if attacker == 'ai':
        return ai_attack(hand, trump_suit)
    show_player_hand(hand)
    choice = valid_choice('Выбери карту(-1: никакая, q: выход): ', -1, len(hand)-1)
    if choice == -1:
        return None
    return hand[choice]

def choose_defense(attack_card, hand, trump_suit, defender):
    if defender == 'ai':
        return ai_defense(attack_card, hand, trump_suit)
    show_player_hand(hand)
    choice = valid_choice('Выбери карту(-1: забрать, q: выход): ', -1, len(hand)-1)
    if choice == -1:
        return None
    return hand[choice]

def take_table(defender_hand, table):
    defender_hand.extend([p['attack'] for p in table])
    defender_hand.extend([p['defense'] for p in table if p['defense']])
    table.clear()

def play_round(attacker_hand, defender_hand, attacker, defender, trump_suit, table, attack_pool=None):
    if attack_pool is None:
        attack_pool = attacker_hand

    attack_card = choose_attack(attack_pool, trump_suit, attacker)
    if attack_card is None:
        return None
    attacker_hand.remove(attack_card)
    add_attack(table, attack_card)
    show_table(table)
    defend_card = choose_defense(attack_card, defender_hand, trump_suit, defender)
    if defend_card is None:
        take_table(defender_hand, table)
        return False
    if can_beat(defend_card, attack_card, trump_suit):
        defender_hand.remove(defend_card)
        add_defense(table, defend_card)
        show_table(table)
    else:
        take_table(defender_hand, table)
        return False
    return True


def turn(attacker_hand, defender_hand, attacker, defender, trump_suit, table):
    result = play_round(attacker_hand, defender_hand, attacker, defender, trump_suit, table)
    if result is None:
        return True
    if not result:
        return False
    while True:
        ranks_on_table = [p['attack'][0] for p in table]
        ranks_on_table += [p['defense'][0] for p in table if p['defense']]
        possible = [c for c in attacker_hand if c[0] in ranks_on_table]
        if not possible or len(table) >= 6:
            break
        print('Можно подкинуть!')
        result = play_round(attacker_hand, defender_hand, attacker, defender, trump_suit, table, attack_pool=possible)
        if result is None:
            break
        if not result:
            return False
    return True

