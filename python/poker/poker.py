from collections import Counter

non_numeric = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def best_hands(hands: list[str]) -> list[str]:
    hands_sep = [element.split() for element in hands]
    hands_num = [[element[:- 1] for element in sublist] for sublist in hands_sep]
    hands_suit = [[element[- 1] for element in sublist] for sublist in hands_sep]



    # straight flush
    straight_flush = []
    for i, hand in enumerate(hands_num):
        if check_straight(hand) and check_flush(hands_suit[i]):
            straight_flush.append(i)
    if len(straight_flush) == 1:
        return [hands[straight_flush[0]]]
    if len(straight_flush) > 1:
        return [hands[i] for i in check_high_card(hands_num)]

    index_winner, outcome_winner = mult_occur(hands_num)
    # four of a kind
    if outcome_winner == 'four_of_a_kind':

        return [hands[index_winner]]

    # full house
    if outcome_winner == 'full_house':
        return [hands[index_winner]]


    ## flush
    flushes = []
    for i, hand in enumerate(hands_suit):
        if check_flush(hand):
            flushes.append(i)
    if len(flushes) == 1:
        return [hands[flushes[0]]]
    if len(flushes) > 1:
        pass

    ## check straight
    straights = []
    for i, hand in enumerate(hands_num):
        if check_straight(hand):
            straights.append(i)
    if len(straights) == 1:
        return [hands[straights[0]]]

    ## three of a kind
    if outcome_winner == 'three_of_a_kind':
        return [hands[index_winner]]

    if outcome_winner == 'pairs':
        return [hands[index_winner]]





    # highest card
    highest_card = check_high_card(hands_num)
    return [hands[i] for i in highest_card]

def check_straight(hand: list[str]):
    ace = False
    if 'A' in hand:
        ace = True
    hand_int = [int(element) if element.isnumeric() else non_numeric[element] for element in hand]
    max_hand = max(hand_int)
    min_hand = min(hand_int)
    straight = list(range(min_hand, max_hand + 1))
    if ace:
        hand_int_ace = [element if element != 14 else 1 for element in hand_int]
        max_hand = max(hand_int_ace)
        min_hand = min(hand_int_ace)
        straight_ace = list(range(min_hand, max_hand + 1))
        return straight == sorted(hand_int) or straight_ace == sorted(hand_int_ace)
    return straight == sorted(hand_int)

def check_flush(hand_suit: list[str]):
    counted_hand = Counter(hand_suit)
    if 5 in counted_hand.values():
        return True
    return False

def check_high_card(hands_num: list[list[str]]):
    if any(isinstance(element, str) for sublist in hands_num for element in sublist):
        hands_num = [[int(element) if element.isnumeric() else non_numeric[element] for element in sublist] for sublist in hands_num]
    max_values = [max(hand) for hand in hands_num]
    max_value = max(max_values)
    if len(set(max_values)) == 1 and all(len(hand) >= 2 for hand in hands_num):
        num_cards = [list(reversed(sorted(hand))) for hand in hands_num]
        without_max = [hand[1:] for hand in num_cards]
        return check_high_card(without_max)
    max_indices = []
    for i, hand in enumerate(hands_num):
        if max(hand) == max_value:
            max_indices.append(i)
    return max_indices



def mult_occur(hand_nums: list[str]):
    max_hand_rep = []
    counted_hands = [dict(Counter(hand)) for hand in hand_nums]
    for hand in counted_hands:
        max_hand_rep.append(max(hand.values()))
    max_rep_value = max(max_hand_rep)
    outcome = ''
    if any(4 in counter.values() for counter in counted_hands):
        outcome = 'four_of_a_kind'
    elif any(3 in counter.values() and 2 in counter.values() for counter in counted_hands):
        outcome = 'full_house'
    elif any(3 in counter.values() for counter in counted_hands):
        outcome = 'three_of_a_kind'
    elif any(2 in counter.values() for counter in counted_hands):
        outcome = 'pairs'
    print(max_hand_rep)
    if len(max_hand_rep) == len(set(max_hand_rep)):
        hand_seq = max_hand_rep.index(max_rep_value)
        return hand_seq, outcome
    else:
        if all(max(max_hand_rep) == rep for rep in max_hand_rep):
            check_tie = []
            for counter in counted_hands:
                count_num = 0
                for item in counter.values():
                    if item == max_rep_value:
                        count_num += 1
                check_tie.append(count_num)
            ### hier anpassen print(max(check_tie))
            if any(element != max(check_tie) for element in check_tie):
                return check_tie.index(max(check_tie)), outcome

            rep_values = []
            for counter in counted_hands:
                for k, v in counter.items():
                    if v == max_rep_value:
                        rep_values.append(k)
            highest_value = max(rep_values)

            highest_hand = (i for i, hand in enumerate(counted_hands) if hand.get(highest_value) == max_rep_value)
            return next(highest_hand), outcome




print(best_hands(["3S 3H 2S 3D 3C", "3S 3H 4S 3D 3C"]))