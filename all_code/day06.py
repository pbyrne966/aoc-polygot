from typing import List, Tuple
from running_wrapper import datawrap

def is_unique(data_point: str, fixed_point: int = 4):
    unq_chars = ''

    for ch in data_point:
        if not unq_chars.find(ch) >= 0:
            unq_chars+=ch
        else:
            return False

    return len(unq_chars) == fixed_point


@datawrap
def parse(data: List[str]) -> Tuple[int, int]:
    pt_one_pnt = 4
    pt_two_pnt = 14

    result_one, result_two = 0,0
    str_data = ''.join(data)
    r_t = len(str_data)

    for idx in range(r_t):
        p_one = str_data[idx:idx+pt_one_pnt]
        if not result_one and is_unique(p_one):
            result_one =  str_data.find(p_one)

        if not result_two and idx + pt_two_pnt <= r_t:
            p_two = str_data[idx:idx+pt_two_pnt]
            if is_unique(p_two):
                result_two = str_data.find(p_two)

        if result_one and result_two:
            break

    return result_one, result_two
