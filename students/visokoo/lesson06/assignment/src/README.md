# cProfile Results

## From cProfilev on poor_perf.py - 1st Pass

```bash
Sun May 19 12:12:14 2019    profile_output.bin

         1115394 function calls (1115376 primitive calls) in 9.729 seconds

   Ordered by: internal time
   List reduced from 137 to 1 due to restriction <'analyze'>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    9.438    9.438    9.634    9.634 poor_perf.py:9(analyze)


Called By:
   Ordered by: internal time
   List reduced from 137 to 1 due to restriction <'analyze'>

Function                 was called by...
                             ncalls  tottime  cumtime
poor_perf.py:9(analyze)  <-       1    9.438    9.634  poor_perf.py:59(main)


Called:
   Ordered by: internal time
   List reduced from 137 to 1 due to restriction <'analyze'>

Function                 called...
                             ncalls  tottime  cumtime
poor_perf.py:9(analyze)  ->   56782    0.048    0.115  /usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/lib/python3.7/codecs.py:319(decode)
                                  2    0.000    0.000  {built-in method _csv.reader}
                                  2    0.000    0.000  {built-in method builtins.print}
                                  2    0.000    0.001  {built-in method io.open}
                                  2    0.000    0.000  {built-in method now}
                            1000000    0.080    0.080  {method 'append' of 'list' objects}
```

- Realized that the datetime comparison wasn't actually working as the second field is not an actual date. Switched from string to actual datetime object.
- This made the program extremely slow (~34 seconds) because it was making every date a valid date object and checking the conditional.
- Removed the redundant line of converting the row to a list as it's already a list.
- Noticed that 2018 is never incremented after running the script and discovered a typo in the if block for bumping the count. Corrected that.
- Combined `with` open statements to one for the searching of `ao` so we're not opening the file twice.
- Instead of using conditional logic to check if the date is greater than 2012, use the date as a key instead and continue if it doesn't exist. Dropped perf to 4.54 seconds on analyze func.

```bash
Sun May 19 15:14:05 2019    profile_output.bin

         137947 function calls (137059 primitive calls) in 4.545 seconds

   Ordered by: internal time
   List reduced from 724 to 1 due to restriction <'analyze'>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    4.272    4.272    4.330    4.330 good_perf.py:31(analyze)


Called By:
   Ordered by: internal time
   List reduced from 724 to 1 due to restriction <'analyze'>

Function                  was called by...
                              ncalls  tottime  cumtime
good_perf.py:31(analyze)  <-       1    4.272    4.330  good_perf.py:79(main)


Called:
   Ordered by: internal time
   List reduced from 724 to 1 due to restriction <'analyze'>

Function                  called...
                              ncalls  tottime  cumtime
good_perf.py:31(analyze)  ->   28390    0.024    0.057  /usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/lib/python3.7/codecs.py:319(decode)
                                   1    0.000    0.000  {built-in method _csv.reader}
                                   1    0.000    0.000  {built-in method builtins.next}
                                   2    0.000    0.000  {built-in method builtins.print}
                                   1    0.000    0.001  {built-in method io.open}
                                   2    0.000    0.000  {built-in method now}
```

## Output from script

```bash
{'2013': 20193, '2014': 20119, '2015': 20483, '2016': 20217, '2017': 20163, '2018': 20255, '2019': 7659}
'ao' was found 0 times
```

## Passing test_perf.py

```bash
python3 -m pytest -vvv ../tests/test_perf.py -vvv
========================================================= test session starts ==========================================================
platform darwin -- Python 3.7.3, pytest-4.2.1, py-1.7.0, pluggy-0.8.1 -- /usr/local/opt/python/bin/python3.7
cachedir: .pytest_cache
rootdir: /Users/vivian/PycharmProjects/_pythoncert_q2/Python220A_2019/students/visokoo/lesson06/assignment, inifile:
plugins: datafiles-2.0
collected 1 item

../tests/test_perf.py::test_assess_preformance PASSED
```