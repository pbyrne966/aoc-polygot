from copy import deepcopy
from typing import List, Tuple, Dict
from collections import defaultdict
from pathlib import Path

def datawrap(fn):

    def get_fn() -> str:
        name = Path(__file__).name
        return ''.join(i for i in name if i.isdigit())

    def wrap(*args, **kwargs):
        _fn = get_fn()
        input_path = Path('.') / 'input'
        with open(f'{input_path}/{_fn}.txt') as f:
            data = f.read().splitlines()

        matrix, cmds =  fn(data)
        return matrix, cmds
    return wrap


@datawrap
def get_matrix(data: List[str]) -> Tuple[Dict[str, List], List[str]]:
    matrix_end_idx = data.index('')
    matrix, cmds = data[:matrix_end_idx], data[matrix_end_idx+1:]

    last_elem = matrix.pop()
    run_length = len(matrix)
    parsed_matrix = defaultdict(list)

    for idx, num in enumerate(last_elem):
        if not num.isspace():
            for depth in reversed(range(run_length)):
                strs = matrix[depth][idx]
                if strs.isspace():
                    break
                parsed_matrix[num].append(strs)

    return parsed_matrix, cmds


def parse_nums(cmd: str) -> Tuple[str, str, str]:
    commands = []
    holding_string:str = ''

    chrs: str
    for chrs in cmd:
        if chrs.isdigit():
            holding_string = holding_string + chrs
            continue
        if chrs.isspace and holding_string != '':
            commands.append(holding_string)
            holding_string=''

    commands.extend([holding_string])
    return tuple(filter(None, commands))


def run() -> Tuple[str, str]:
    mtx, cmds = get_matrix() # type: ignore
    part_two: Dict[str, List] = dict(deepcopy(mtx))

    cmd: str
    for cmd in cmds:
        amt, frm , to = parse_nums(cmd)
        amt = int(amt)

        for _ in range(amt):
            take = mtx[frm]
            if not take:
                break
            move = take.pop()
            mtx[to].append(move)

        pt_two_take = part_two[frm]
        move = pt_two_take[-amt:]
        part_two[frm] = pt_two_take[:-amt]
        part_two[to].extend(move)

    pt_one = ''.join([i[-1] for i in mtx.values()])
    pt_two = ''.join([i[-1] for i in part_two.values()])
    return pt_one, pt_two

@datawrap
def test(data: List[str]):

    COMPARE_DATA = {
        '1': ['Z', 'J', 'G'],
        '2': ['Q','L','R','P','W','F','V','C'],
        '3': ['F','P','M','C','L','G','R'],
        '4': ['L', 'F', 'B', 'W', 'P', 'H', 'M'],
        '5': ['G', 'C', 'F', 'S', 'V', 'Q'],
        '6': ['W', 'H', 'J', 'Z', 'M', 'Q', 'T', 'L'],
        '7': ['H', 'F', 'S', 'B', 'V'],
        '8': ['F', 'J', 'Z', 'S'],
        '9': ['M', 'C', 'D', 'P', 'F','H', 'B', 'T'],
    }

    compiled_result, _ = get_matrix(data)
    assert list(COMPARE_DATA.keys()) == list(compiled_result.keys())
    assert all(
        compiled_result.get(k) == v
        for k,v in COMPARE_DATA.items()
    )
    pt_one, pt_two = run()
    assert pt_one == 'WSFTMRHPP'
    assert pt_two == 'GSLCMFBRP'
    return True


if __name__ == "__main__":
    _, pt_two = run()
    print(pt_two)