from typing import List

NUMBERS_MAPPING = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def read_input_file(path: str) -> List[str]:
    with open(path, "r") as file:
        lines = [line.strip('\n') for line in file]
    return lines


def convert_spelling_to_digits(l: List[str]) -> List[str]:
    transformed = []
    for s in l:
        transformed_str = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                transformed_str += s[i]
                i += 1
            else:
                flag = False
                for spelling, number in NUMBERS_MAPPING.items():
                    if s[i:].startswith(spelling):
                        flag = True
                        transformed_str += str(number)
                        i += len(spelling)-1
                        break
                if not flag:
                    transformed_str += s[i]
                    i += 1
        transformed.append(transformed_str)
    return transformed


def get_numbers_from_strings(lines: List[str]) -> List[int]:
    nums = []
    for line in lines:
        l_ptr = 0
        r_ptr = len(line) - 1
        while l_ptr < len(line):
            if line[l_ptr].isdigit():
                break
            l_ptr += 1
        while r_ptr >= 0:
            if line[r_ptr].isdigit():
                break
            r_ptr -= 1
        nums.append(int(f"{line[l_ptr]}{line[r_ptr]}"))
    return nums


if __name__ == "__main__":
    print(sum(get_numbers_from_strings(read_input_file("input.txt"))))
    print(sum(get_numbers_from_strings(convert_spelling_to_digits(read_input_file("input.txt")))))
