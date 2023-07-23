from running_wrapper import datawrap, get_fn
from typing import List


@datawrap(_fn=get_fn())
def parse(data: List[str]):
    print(data)






if __name__ == "__main__":
    tester_one = '202988 zcdtsqq.qfv'
    tester_two = '135422 zpdlcd'
    tester_three = 'cd fscnr'
    parse()




