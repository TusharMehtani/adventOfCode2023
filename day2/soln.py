from typing import List

CONSTRAINTS = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def parse_subsets(subsets: str) -> dict[int, dict]:
    parsed = {}
    for subset in subsets.split(";"):
        for color in subset.split(","):
            color_cnt, color_name = color.split()
            if color_name in parsed:
                parsed[color_name] = max(parsed[color_name], int(color_cnt))
            else:
                parsed[color_name] = int(color_cnt)
    return parsed


def get_input_from_file(path: str) -> dict[int, dict]:
    parsed = {}
    with open(path, "r") as f:
        for line in f:
            game_id, subsets = line.split(":")
            game_id = int(game_id.split()[1])
            parsed[game_id] = parse_subsets(subsets)
    return parsed


def check_if_game_is_possible(game: dict) -> bool:
    for color, color_cnt in game.items():
        if color_cnt > CONSTRAINTS[color]:
            return False
    return True


def calculate_power(games: dict[int, dict]) -> int:
    ans = 0
    for game_id, colors in games.items():
        power = 1
        for color_name, color_cnt in colors.items():
            power *= color_cnt
        ans += power
    return ans


if __name__ == "__main__":
    games = get_input_from_file("./input.txt")
    ans = 0
    for game_id, color_cnts in games.items():
        if check_if_game_is_possible(color_cnts):
            ans += game_id
    print(ans)
    print(calculate_power(games))
