"""
    You will submit two modules: linear.py and parallel.py
    Each module will return a list of tuples, one tuple for
     customer and one for products.
    Each tuple will contain 4 values: the number of records processed,
    the record count in the database prior to running, the record count
    after running,
    and the time taken to run the module.

"""

import sys
import os

loc = str(os.getcwd()[:-3] + 'src')
# C:\Python220\Lesson07\Homework\assignment\src
# C:\Python220\Lesson07\Homework\assignment\src
sys.path.append("r'{}'".format(loc))


print("r'{}'".format(loc))

import pytest
import test as db
import parallel as p

answers_parallel = p.run_parallel()

test =         {
        "processed": answers_parallel[1][0],
        "count_prior": answers_parallel[1][1],
        "count_new": answers_parallel[1][2],
        "elapsed": answers_parallel[1][3]
        }

print(test)