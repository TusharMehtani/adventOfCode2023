from typing import List


def get_adjacent_diffs(lst):
    return [second - first for first, second in zip(lst, lst[1:])]


def get_prev_num(x: List[int]) -> int:
    if all([_ == 0 for _ in x]):
        return 0
    return x[0] - get_prev_num(get_adjacent_diffs(x))


def get_next_num(x: List[int]) -> int:
    if all([_ == 0 for _ in x]):
        return 0
    return x[-1] + get_next_num(get_adjacent_diffs(x))


def parse_input_file(path: str) -> List[List[int]]:
    inputs = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip().split()
            inputs.append([int(x) for x in line])
    return inputs


if __name__ == "__main__":
    inputs = parse_input_file("input.txt")

    # part 1
    next_nums = 0
    for idx, ip in enumerate(inputs):
        next_nums += get_next_num(ip)
    print(next_nums)

    # part 2
    prev_nums = 0
    for idx, ip in enumerate(inputs):
        prev_nums += get_prev_num(ip)
    print(prev_nums)
