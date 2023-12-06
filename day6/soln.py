import time as python_time
from typing import List


def get_soln_cnts(time: int, distance: int) -> int:
    soln_cnt = 0
    soln1 = (time - (time ** 2 - 4 * distance) ** 0.5) / 2
    soln2 = (time + (time ** 2 - 4 * distance) ** 0.5) / 2
    for hold_time in range(0, time):
        if soln1 < hold_time < soln2:
            soln_cnt += 1
    return soln_cnt


def parse_input_file(path: str) -> (List[int], List[int]):
    with open(path, "r") as f:
        times = f.readline().split(":")[1].strip().split()
        times = [int(x) for x in times]
        distances = f.readline().split(":")[1].strip().split()
        distances = [int(x) for x in distances]
        return times, distances

def parse_input_file_part2(path: str) -> (int, int):
    with open(path, "r") as f:
        time = int("".join(f.readline().split(":")[1].strip().split()))
        distance = int("".join(f.readline().split(":")[1].strip().split()))
        return time, distance

if __name__ == "__main__":
    times, distances = parse_input_file("./input.txt")
    soln_cnts = 1
    for time, distance in zip(times, distances):
        soln_cnt = get_soln_cnts(time, distance)
        soln_cnts *= soln_cnt
    print(soln_cnts)

    start_time = python_time.perf_counter()
    time,distance = parse_input_file_part2("./input.txt")
    end_time = python_time.perf_counter()
    runtime_in_seconds = end_time - start_time
    print(get_soln_cnts(time,distance))
    print(f"Runtime: {runtime_in_seconds} seconds")

