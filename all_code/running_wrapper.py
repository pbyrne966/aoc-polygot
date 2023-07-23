from pathlib import Path


def get_fn() -> str:
        name = Path(__file__).name
        return ''.join(i for i in name if i.isdigit())

def datawrap(fn, _fn):

    def wrap(*args, **kwargs):
        # _fn = get_fn()
        input_path = Path('.') / 'input'
        with open(f'{input_path}/{_fn}.txt') as f:
            data = f.read().splitlines()

        matrix, cmds =  fn(data)
        return matrix, cmds
    return wrap