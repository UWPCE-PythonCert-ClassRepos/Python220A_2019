"""
check good works the same, and is faster
"""
import sys
import pytest

sys.path.append(r'N:\Python220\lesson06\Lesson06\assignment\src')
import poor_perf as p
import good_perf as g
import pandas_perf as n


def test_assess_preformance():
    """ compare """
    poor = p.analyze(r'N:\Python220\lesson06\Lesson06\assignment\src\test.csv')
    good = g.analyze(r'N:\Python220\lesson06\Lesson06\assignment\src\test.csv')
    new = n.analyze(r'N:\Python220\lesson06\Lesson06\assignment\src\test.csv')
    poor_elapsed = poor[0]
    good_elapsed = good[0]
    new_elapsed = new[0]

    print(f'poor: {poor_elapsed}')
    print(f'good: {good_elapsed}')
    print(f'new: {new_elapsed}')

    assert good_elapsed < poor_elapsed
    assert poor[2] == good[2] == new[2]
    assert good[1] == new[1]

# poor: 18.53240704536438
# good: 3.6633636951446533
# new: 4.28194785118103

