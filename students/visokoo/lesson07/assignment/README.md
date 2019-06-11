### First run with cProfile on existing import logic

With 10 rows of data:

```
        236005 function calls (229635 primitive calls) in 0.815 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    430/1    0.005    0.000    0.815    0.815 {built-in method builtins.exec}
        1    0.000    0.000    0.815    0.815 src/database.py:4(<module>)
   813/12    0.005    0.000    0.684    0.057 <frozen importlib._bootstrap>:978(_find_and_load)
   813/12    0.003    0.000    0.683    0.057 <frozen importlib._bootstrap>:948(_find_and_load_unlocked)
   790/14    0.001    0.000    0.680    0.049 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
    441/8    0.003    0.000    0.680    0.085 <frozen importlib._bootstrap>:663(_load_unlocked)
    379/7    0.002    0.000    0.679    0.097 <frozen importlib._bootstrap_external>:722(exec_module)
        1    0.000    0.000    0.575    0.575 /usr/local/lib/python3.7/site-packages/pandas/__init__.py:5(<module>)
   574/82    0.001    0.000    0.443    0.005 {built-in method builtins.__import__}
      379    0.007    0.000    0.295    0.001 <frozen importlib._bootstrap_external>:793(get_code)
        1    0.000    0.000    0.237    0.237 /usr/local/lib/python3.7/site-packages/pandas/core/api.py:5(<module>)
2646/1638    0.002    0.000    0.224    0.000 <frozen importlib._bootstrap>:1009(_handle_fromlist)
      379    0.023    0.000    0.187    0.000 <frozen importlib._bootstrap_external>:914(get_data)
      379    0.164    0.000    0.164    0.000 {method 'read' of '_io.FileIO' objects}
        1    0.000    0.000    0.156    0.156 /usr/local/lib/python3.7/site-packages/pandas/core/groupby/__init__.py:1(<module>)
        1    0.000    0.000    0.140    0.140 /usr/local/lib/python3.7/site-packages/pandas/core/groupby/groupby.py:8(<module>)
        1    0.000    0.000    0.136    0.136 src/database.py:33(import_data)
        1    0.000    0.000    0.133    0.133 /usr/local/lib/python3.7/site-packages/pandas/core/frame.py:12(<module>)
        1    0.000    0.000    0.123    0.123 /usr/local/lib/python3.7/site-packages/numpy/__init__.py:106(<module>)
  440/424    0.001    0.000    0.120    0.000 <frozen importlib._bootstrap>:576(module_from_spec)
        3    0.000    0.000    0.112    0.037 /usr/local/lib/python3.7/site-packages/pymongo/collection.py:696(insert_many)
        3    0.000    0.000    0.111    0.037 /usr/local/lib/python3.7/site-packages/pymongo/bulk.py:499(execute)
```
### Linear run:
With 10000 rows of data:

```
         1759919 function calls (1753483 primitive calls) in 1.328 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    430/1    0.003    0.000    1.328    1.328 {built-in method builtins.exec}
        1    0.003    0.003    1.328    1.328 src/database.py:4(<module>)
        1    0.003    0.003    0.944    0.944 src/database.py:34(import_data)
        3    0.000    0.000    0.536    0.179 /usr/local/lib/python3.7/site-packages/pymongo/collection.py:696(insert_many)
        3    0.015    0.005    0.396    0.132 src/database.py:92(csv_to_list_dict)
   813/12    0.004    0.000    0.387    0.032 <frozen importlib._bootstrap>:978(_find_and_load)
   813/12    0.002    0.000    0.387    0.032 <frozen importlib._bootstrap>:948(_find_and_load_unlocked)
   790/14    0.000    0.000    0.383    0.027 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
    441/8    0.002    0.000    0.383    0.048 <frozen importlib._bootstrap>:663(_load_unlocked)
    379/7    0.001    0.000    0.382    0.055 <frozen importlib._bootstrap_external>:722(exec_module)
        3    0.000    0.000    0.370    0.123 /usr/local/lib/python3.7/site-packages/pymongo/bulk.py:499(execute)
        3    0.000    0.000    0.370    0.123 /usr/local/lib/python3.7/site-packages/pymongo/bulk.py:322(execute_command)
        3    0.000    0.000    0.369    0.123 /usr/local/lib/python3.7/site-packages/pymongo/mongo_client.py:1164(_retry_with_session)
        3    0.000    0.000    0.369    0.123 /usr/local/lib/python3.7/site-packages/pymongo/bulk.py:338(retryable_bulk)
        3    0.001    0.000    0.369    0.123 /usr/local/lib/python3.7/site-packages/pymongo/bulk.py:247(_execute_command)
        1    0.000    0.000    0.330    0.330 /usr/local/lib/python3.7/site-packages/pandas/__init__.py:5(<module>)
        3    0.000    0.000    0.314    0.105 /usr/local/lib/python3.7/site-packages/pandas/core/frame.py:1195(to_dict)
        3    0.054    0.018    0.310    0.103 /usr/local/lib/python3.7/site-packages/pandas/core/frame.py:1310(<listcomp>)
   574/82    0.001    0.000    0.255    0.003 {built-in method builtins.__import__}
        3    0.000    0.000    0.213    0.071 /usr/local/lib/python3.7/site-packages/pymongo/message.py:912(write_command)
        3    0.000    0.000    0.213    0.071 /usr/local/lib/python3.7/site-packages/pymongo/pool.py:641(write_command)
       11    0.000    0.000    0.213    0.019 /usr/local/lib/python3.7/site-packages/pymongo/network.py:169(receive_message)
       22    0.000    0.000    0.213    0.010 /usr/local/lib/python3.7/site-packages/pymongo/network.py:226(_receive_data_on_socket)
       22    0.212    0.010    0.212    0.010 {method 'recv_into' of '_socket.socket' objects}
        3    0.000    0.000    0.211    0.070 /usr/local/lib/python3.7/site-packages/pymongo/pool.py:603(receive_message)
   209979    0.058    0.000    0.188    0.000 /usr/local/lib/python3.7/site-packages/pandas/core/frame.py:1310(<genexpr>)
        3    0.004    0.001    0.166    0.055 /usr/local/lib/python3.7/site-packages/pymongo/collection.py:752(<listcomp>)
    30000    0.029    0.000    0.163    0.000 /usr/local/lib/python3.7/site-packages/pymongo/collection.py:740(gen)
        3    0.000    0.000    0.133    0.044 /usr/local/lib/python3.7/site-packages/pymongo/message.py:1266(_do_bulk_write_command)
        3    0.000    0.000    0.133    0.044 /usr/local/lib/python3.7/site-packages/pymongo/message.py:1182(_do_batched_op_msg)
        3    0.122    0.041    0.133    0.044 {built-in method pymongo._cmessage._batched_op_msg}
   179982    0.080    0.000    0.130    0.000 /usr/local/lib/python3.7/site-packages/pandas/core/common.py:79(maybe_box_datetimelike)
        1    0.000    0.000    0.125    0.125 /usr/local/lib/python3.7/site-packages/pandas/core/api.py:5(<module>)
2670/1662    0.002    0.000    0.125    0.000 <frozen importlib._bootstrap>:1009(_handle_fromlist)
   433227    0.072    0.000    0.123    0.000 {built-in method builtins.isinstance}

Importing data start time:  2019-06-01 21:11:20.783265
Done importing end time:  2019-06-01 21:11:21.729691 total time: 0:00:00.946426
```

### Parallel run
Refactored the import data function to handle one csv at a time and created a main() method 
that handles the threading. A new thread is started for each csv passed to add data to the
mongodb collection. Saw about a .2 second improvement.

With 10000 rows of data:

```
215059 function calls (209239 primitive calls) in 1.128 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    422/1    0.003    0.000    1.128    1.128 {built-in method builtins.exec}
        1    0.000    0.000    1.128    1.128 src/parallel.py:4(<module>)
        1    0.000    0.000    0.731    0.731 src/parallel.py:116(main)
       15    0.729    0.049    0.729    0.049 {method 'acquire' of '_thread.lock' objects}
        3    0.000    0.000    0.728    0.243 /usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/lib/python3.7/threading.py:1000(join)
        3    0.000    0.000    0.728    0.243 /usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/lib/python3.7/threading.py:1038(_wait_for_tstate_lock)
    780/4    0.003    0.000    0.397    0.099 <frozen importlib._bootstrap>:978(_find_and_load)
    780/4    0.002    0.000    0.397    0.099 <frozen importlib._bootstrap>:948(_find_and_load_unlocked)
    433/5    0.002    0.000    0.395    0.079 <frozen importlib._bootstrap>:663(_load_unlocked)
    371/4    0.001    0.000    0.395    0.099 <frozen importlib._bootstrap_external>:722(exec_module)
    760/5    0.000    0.000    0.394    0.079 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
        1    0.000    0.000    0.340    0.340 /usr/local/lib/python3.7/site-packages/pandas/__init__.py:5(<module>)
   551/74    0.001    0.000    0.260    0.004 {built-in method builtins.__import__}
        1    0.000    0.000    0.138    0.138 /usr/local/lib/python3.7/site-packages/pandas/core/api.py:5(<module>)
2520/1514    0.002    0.000    0.129    0.000 <frozen importlib._bootstrap>:1009(_handle_fromlist)
      371    0.003    0.000    0.100    0.000 <frozen importlib._bootstrap_external>:793(get_code)
        1    0.000    0.000    0.097    0.097 /usr/local/lib/python3.7/site-packages/pandas/core/groupby/__init__.py:1(<module>)
        1    0.000    0.000    0.088    0.088 /usr/local/lib/python3.7/site-packages/pandas/core/groupby/groupby.py:8(<module>)
        1    0.000    0.000    0.084    0.084 /usr/local/lib/python3.7/site-packages/pandas/core/frame.py:12(<module>)
        1    0.000    0.000    0.082    0.082 /usr/local/lib/python3.7/site-packages/numpy/__init__.py:106(<module>)
  432/416    0.001    0.000    0.071    0.000 <frozen importlib._bootstrap>:576(module_from_spec)
      371    0.001    0.000    0.062    0.000 <frozen importlib._bootstrap_external>:523(_compile_bytecode)
      371    0.060    0.000    0.060    0.000 {built-in method marshal.loads}
    57/42    0.000    0.000    0.060    0.001 <frozen importlib._bootstrap_external>:1040(create_module)
    57/42    0.040    0.001    0.060    0.001 {built-in method _imp.create_dynamic}
  947/943    0.016    0.000    0.057    0.000 {built-in method builtins.__build_class__}
      605    0.004    0.000    0.056    0.000 <frozen importlib._bootstrap>:882(_find_spec)
        1    0.000    0.000    0.053    0.053 /usr/local/lib/python3.7/site-packages/pymongo/__init__.py:15(<module>)
      602    0.001    0.000    0.048    0.000 <frozen importlib._bootstrap_external>:1272(find_spec)
      602    0.002    0.000    0.048    0.000 <frozen importlib._bootstrap_external>:1240(_get_spec)
        1    0.000    0.000    0.043    0.043 /usr/local/lib/python3.7/site-packages/pandas/core/generic.py:2(<module>)
      834    0.008    0.000    0.042    0.000 <frozen importlib._bootstrap_external>:1356(find_spec)
      613    0.004    0.000    0.041    0.000 /usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/lib/python3.7/textwrap.py:414(dedent)
        1    0.000    0.000    0.040    0.040 /usr/local/lib/python3.7/site-packages/pandas/core/arrays/__init__.py:1(<module>)
      551    0.001    0.000    0.039    0.000 /usr/local/lib/python3.7/site-packages/pandas/util/_decorators.py:310(__call__)
        1    0.000    0.000    0.035    0.035 /usr/local/lib/python3.7/site-packages/numpy/core/__init__.py:1(<module>)
        1    0.000    0.000    0.034    0.034 /usr/local/lib/python3.7/site-packages/pytz/__init__.py:9(<module>)
      215    0.000    0.000    0.032    0.000 {method 'extend' of 'list' objects}
```