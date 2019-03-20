import os
import sys
import datetime

# import pytest

path = os.path.dirname(os.path.abspath(__file__))
path, _ = os.path.split(path)
path = os.path.join(path, 'src')

sys.path.insert(len(sys.path), path)

from src.BrilliantImagery.sequence import Sequence


def test_stabelize():
    s = Sequence('E:\\Pictures\\2016\\2016-12-19')
    s.stabilize([0.5, 0.65, 0.7, 0.85], 7, True)
    s.save()


def test_reamp():
    s = Sequence('E:\\Pictures\\2016\\2016-12-19')
    s.ramp([0.5, 0.65, 0.7, 0.85])
    s.save()


def test_ramp_and_stabilize():
    s = Sequence('E:\\Pictures\\2016\\2016-12-19')
    s.ramp_and_stabilize([0.5, 0.65, 0.7, 0.85])
    s.save()


def main():
    # test_stabelize() G:\Pictures\2017\2017-05-03\tl
    # test_reamp()
    # test_ramp_and_stabilize()
    t1 = datetime.datetime.now()
    print('zero', t1)
    # s = Sequence('G:\\Pictures\\Timelapse\\20161220_test_sequence')
    s = Sequence('G:\\Pictures\\2017\\2017-05-03\\tl')
    # s = Sequence('G:\\Pictures\\2018\\2018-10-26')
    # s.ramp_minus_exmpsure()
    # s.ramp_exposure([0.5, 0.65, 0.7, 0.85])
    s.ramp([0.01, 0.33, 0.35, 0.66])
    print('one', datetime.datetime.now(), datetime.datetime.now() - t1)
    # s.ramp_and_stabilize([0.5, 0.65, 0.7, 0.85], 8)
    s.ramp_and_stabilize([0.6, 0.7, 0.85, 1.0], 10)
    # s.ramp([0.05, 0.2, 0.35, 0.5])
    print('two', datetime.datetime.now(), datetime.datetime.now() - t1)
    # s.stabilize([0.5, 0.65, 0.7, 0.85], 8)
    # s.save()
    print('three', datetime.datetime.now(), datetime.datetime.now() - t1)


if __name__ == '__main__':
    main()

# 16.7
