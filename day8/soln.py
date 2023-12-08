import re
from typing import Tuple

pattern = r'\b[A-Za-z0-9]{3}\b'
START = "AAA"
DESTINATION = "ZZZ"

def calculate_lcm(numbers):
    """Calculate the least common multiple (LCM) of a list of integers."""

    def gcd(a, b):
        """Calculate the greatest common divisor (GCD) of two numbers using Euclidean algorithm."""
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        """Calculate the least common multiple (LCM) of two numbers using GCD."""
        return (a * b) // gcd(a, b)

    lcm_result = numbers[0]
    for i in range(1, len(numbers)):
        lcm_result = lcm(lcm_result, numbers[i])

    return lcm_result
def check_condition(curr_pos: str, destination: str, part1: bool) -> bool:
    if part1:
        return curr_pos == destination
    return curr_pos[-1] == "Z"


def traverse(instructions: str, directions: dict[str, dict], start: str, destination: str = None,
             part1: bool = True) -> int:
    ins_ptr = 0
    curr_pos = start
    steps = 0
    if curr_pos not in directions:
        return 0
    while not check_condition(curr_pos, destination, part1):
        ins = instructions[ins_ptr % len(instructions)]
        curr_pos = directions[curr_pos][ins]
        steps += 1
        ins_ptr += 1
    return steps


def parse_input_file(path: str) -> Tuple[str, dict[str, dict]]:
    directions = {}
    with open(path, "r") as f:
        instructions = f.readline().strip()
        for line in f:
            line = line.strip()
            if line == "":
                continue
            matches = re.findall(pattern, line)
            assert len(matches) == 3, "Improperly formatted file"
            if matches[0] not in directions:
                directions[matches[0]] = {
                    'L': matches[1],
                    'R': matches[2]
                }
    return instructions, directions


if __name__ == "__main__":
    instructions, directions = parse_input_file("input.txt")

    # part 1
    print(traverse(instructions, directions, START, DESTINATION))

    # part 2
    all_steps = []
    for position, dirs in directions.items():
        if position[-1] == "A":
            steps = traverse(instructions, directions, position, part1=False)
            all_steps.append(steps)
    print(calculate_lcm(all_steps))
