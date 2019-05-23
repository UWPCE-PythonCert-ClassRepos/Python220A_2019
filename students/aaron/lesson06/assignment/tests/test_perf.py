"""
check good works the same, and is faster
"""

import src.poor_perf as p
import src.good_perf as g


def test_assess_preformance():
    """ compare """
    g.gen_data('data/generated_data.csv', 1000000)
    poor = p.analyze('data/generated_data.csv')
    good = g.analyze('data/generated_data.csv')
    poor_elapsed = poor[1] - poor[0]
    good_elapsed = good[1] - good[0]
    print("Poor elapsed: %s" % poor_elapsed)
    print("Good elapsed: %s" % good_elapsed)
    assert good_elapsed < poor_elapsed
    assert poor[2] == good[2]
    assert poor[3] == good[3]
