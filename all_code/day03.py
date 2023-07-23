from typing import List, Dict, Tuple
import string

with open('./input/03.txt') as f:
    data = f.read().splitlines()


initial = 0
PRIORITY_MAP = {
    k: idx+1 for idx,k in enumerate(string.ascii_letters)
}

def parse(data: List[str]):
    data_by_split_line = {}
    for idx, row in enumerate(data):
        mid_point = len(row) // 2
        first_half, second_half = row[:mid_point], row[mid_point:]
        data_by_split_line[idx] = first_half, second_half
    return data_by_split_line


def part_one(data: Dict[int, Tuple[str, str]]):
    results = []
    for v in data.values():
        first, second = v
        _first = set(first)
        for elem in second:
            if _first.__contains__(elem):
                amount = PRIORITY_MAP.get(elem)
                results.append(amount)
                break
    return sum(results)


def part_two(data: List[str], chunk_len=3) -> int:
    total = 0
    for i in range(0, len(data), 3):
        current_chunk = data[i:i+chunk_len]
        first_point = current_chunk[0]
        first, second = tuple(current_chunk[1:])

        for char in first_point:
            if first.count(char) and second.count(char):
                total+=PRIORITY_MAP.get(char, 0)
                break

    return total


if __name__ == "__main__":
    data_given = parse(data)
    one = part_one(data_given)
    two = part_two(data)
    print(one, two)
