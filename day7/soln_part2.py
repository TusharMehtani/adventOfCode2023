from typing import List, Tuple
from functools import cmp_to_key

CARDS_TO_STRENGTH = {
    'J': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'Q': 11,
    'K': 12,
    'A': 13
}

HANDS_TO_STRENGTH = {
    'HIGH_CARD': 1,
    'ONE_PAIR': 2,
    'TWO_PAIR': 3,
    'THREE_OF_A_KIND': 4,
    'FULL_HOUSE': 5,
    'FOUR_OF_A_KIND': 6,
    'FIVE_OF_A_KIND': 7
}


def compare_cards(card1: str, card2: str) -> int:
    return CARDS_TO_STRENGTH[card1] - CARDS_TO_STRENGTH[card2]


def compare_hands(a: Tuple[str, int], b: Tuple[str, int]) -> int:
    hand1 = a[0]
    hand2 = b[0]
    hand_comparison = HANDS_TO_STRENGTH[get_hand_type(hand1)] - HANDS_TO_STRENGTH[get_hand_type(hand2)]
    if hand_comparison == 0:
        for card1, card2 in zip(hand1, hand2):
            card_comparison = compare_cards(card1, card2)
            if card_comparison == 0:
                continue
            else:
                return card_comparison
    return hand_comparison


compare_hands_key_function = cmp_to_key(compare_hands)


def get_cards_to_counts(hand: str) -> dict[str, int]:
    cards_to_counts = {}
    for card in hand:
        if card not in cards_to_counts:
            cards_to_counts[card] = 1
        else:
            cards_to_counts[card] += 1
    return cards_to_counts


def get_hand_type(hand: str) -> str:
    if hand == "JJJJJ":
        return "FIVE_OF_A_KIND"
    cards_to_counts = get_cards_to_counts(hand)
    if 'J' in cards_to_counts:
        most_freq_card = ""
        max_freq = 0
        for card, freq in cards_to_counts.items():
            if card != 'J':
                if freq > max_freq:
                    most_freq_card = card
                    max_freq = freq
                elif freq == max_freq:
                    if compare_cards(most_freq_card, card) < 0:
                        most_freq_card = card
                        max_freq = freq
        modified_hand = hand.replace("J", most_freq_card)
        return get_hand_type(modified_hand)
    else:
        if len(cards_to_counts) == 1:
            return "FIVE_OF_A_KIND"
        elif len(cards_to_counts) == 2 and max(cards_to_counts.values()) == 4:
            return "FOUR_OF_A_KIND"
        elif len(cards_to_counts) == 2 and max(cards_to_counts.values()) == 3:
            return "FULL_HOUSE"
        elif len(cards_to_counts) == 3 and max(cards_to_counts.values()) == 3:
            return "THREE_OF_A_KIND"
        elif len(cards_to_counts) == 3 and max(cards_to_counts.values()) == 2:
            return "TWO_PAIR"
        elif len(cards_to_counts) == 4:
            return "ONE_PAIR"
        else:
            return "HIGH_CARD"


def parse_input_file(path: str) -> List[Tuple[str, int]]:
    game = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            hand, bid = line.split()
            game.append((hand, int(bid)))
    return game


if __name__ == "__main__":
    game = parse_input_file("input.txt")
    sorted_game = sorted(game, key=compare_hands_key_function)
    ans = 0
    for idx, x in enumerate(sorted_game):
        ans += (idx + 1) * x[1]
    print(ans)
