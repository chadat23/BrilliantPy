import timeit


def test_decode_time():
    number = 10

    setup = '''
from pathlib import Path

import numpy as np

from brilliantimagery import ljpeg

path = str(Path.cwd().parent / 'tests' / 'data' / 'ljpg_F-18.ljpg')
input_file = np.fromfile(path, np.uint8).astype(np.intc)
    '''

    run = '''
ljpeg.decode(input_file)
    '''

    print('Total ljpg.decode time:', timeit.timeit(run, setup, number=number) / number)

    # 0.1135
