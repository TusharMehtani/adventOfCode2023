from typing import List, Tuple
from functools import cmp_to_key

CARDS_TO_STRENGTH = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 10,
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


def compare_hands(a: Tuple[str,int], b: Tuple[str,int]) -> int:
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


def get_hand_type(hand: str) -> str:
    cards_to_counts = {}
    for card in hand:
        if card not in cards_to_counts:
            cards_to_counts[card] = 1
        else:
            cards_to_counts[card] += 1
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
        ans += (idx+1)*x[1]
    print(ans)