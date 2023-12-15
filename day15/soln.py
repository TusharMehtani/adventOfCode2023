import re
from typing import List

PATTERN = r'([A-Za-z]+)(-|=)(?:([1-9])|$)'
TOTAL_BOXES = 256


def hash(seq: str) -> int:
    curr_val = 0
    for char in seq:
        curr_val += ord(char)
        curr_val *= 17
        curr_val = curr_val % 256
    return curr_val


def parse_input_file(path: str) -> List[str]:
    with open(path, "r") as f:
        return f.readline().strip().split(",")


if __name__ == "__main__":
    init_seq = parse_input_file("input.txt")
    # part 1
    print(sum([hash(x) for x in init_seq]))

    # part 2
    boxes = [[] for _ in range(TOTAL_BOXES)]
    for seq in init_seq:
        label, char, focal_length = re.search(PATTERN, seq).groups()
        box_num = hash(label)
        if char == '-':
            found_idx = -1
            for idx, (lens_label, power) in enumerate(boxes[box_num]):
                if lens_label == label:
                    found_idx = idx
                    break
            if found_idx != -1:
                for idx in range(found_idx, len(boxes[box_num]) - 1):
                    boxes[box_num][idx] = boxes[box_num][idx + 1]
                boxes[box_num].pop()
        elif char == '=':
            found_idx = -1
            for idx, (lens_label, power) in enumerate(boxes[box_num]):
                if lens_label == label:
                    found_idx = idx
                    break
            if found_idx != -1:
                boxes[box_num][found_idx] = (label, focal_length)
            else:
                boxes[box_num].append((label, focal_length))

    ans = 0
    for box_num, box in enumerate(boxes):
        for idx, (lens_label, focal_length) in enumerate(box):
            ans += (box_num+1)*(idx+1)*int(focal_length)
    print(ans)

