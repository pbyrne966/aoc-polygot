from typing import List

with open('./input/01.txt') as f:
    data = f.read().splitlines()

def parse(data: List[str]):
    hold = []
    totals = []
    for line in data:
        if line != '':
            hold.append(int(line))
        else:
            totals.append(sum(hold))
            hold.clear()
    return totals

def part_one(data: List[int]):
    return max(data)

def part_two(data: List[int]):

    data.sort()
    return sum(data[-3:])

if __name__ == "__main__":
    give_data = parse(data)

    print(part_one(give_data))
    print(part_two(give_data))