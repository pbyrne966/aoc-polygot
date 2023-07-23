from typing import List

with open('./input/04.txt') as f:
    data = f.read().splitlines()


def parse_line(row: str):
    return tuple(map(int,row.split('-')))


def parse(data: List[str]):
    part_one = 0
    part_two = 0

    for row in data:
        mid = row.rfind(',')
        first, second = parse_line(row[:mid]), parse_line(row[mid+1:])
        first_one, first_two = first
        second_one, second_two = second
        if (
            first_one <= second_one and second_two <= first_two
            or
            second_one <= first_one and first_two <= second_two
        ):
            part_one+=1

        if first_one <= second_two and second_one <= first_two:
            part_two+=1

    return part_one, part_two


if __name__ == "__main__":
    p1, p2 = parse(
        data
    )
    print(p1, p2)
