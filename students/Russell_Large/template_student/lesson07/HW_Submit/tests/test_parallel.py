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

loc = str(os.getcwd()[:-5] + 'src')
# C:\Python220\Lesson07\Homework\assignment\src
# C:\Python220\Lesson07\Homework\assignment\src
sys.path.append(loc)

print(loc)
import pytest
import test as db
import parallel as p

p.run_parallel(db.import_data)
