import string
import random
import time
import sys
import numpy as np
import create_large_dataset as cr

#### NP.Array & appending f string ####
beginning_time = time.time()
tot_list = []
for i in np.array(range(1, 10000)):
    row = (f'{i},{cr.guid_full_gen()},{i},{i},{cr.get_random_date()},{cr.sentence()}')
    tot_list.append(row)
elapsed_time = time.time()-beginning_time
print(f'NP.Array & appending f string: {elapsed_time}')

#### Map & appending f string ####

beginning_time = time.time()
tot_list2 = []
# change this for loop to another method
for i in map(np.array, range(1, 100000)):
    row = (f'{i},{cr.guid_full_gen()},{i},{i},{cr.get_random_date()},{cr.sentence()}')
    tot_list2.append(row)
elapsed_time = time.time() - beginning_time
print(f'Map & appending f string: {elapsed_time}')


#### NP.Array & appending tuple ####
beginning_time = time.time()
tot_list2 = []
count = 0
# change this for loop to another method
for i in map(np.array, range(1, 100000)):
    generated_data = count, cr.guid_full_gen(), count, count, cr.get_random_date(), cr.ccnum_gen(), cr.sentence()
    count += 1
    tot_list2.append(generated_data)
elapsed_time = time.time() - beginning_time
print(f'NP.Array & appending tuple: {elapsed_time}')

#### Map & appending tuple ####
beginning_time = time.time()
tot_list2 = []
# change this for loop to another method
for i in np.array(range(1, 100000)):
    generated_data = count, cr.guid_full_gen(), count, count, cr.get_random_date(), cr.ccnum_gen(), cr.sentence()
    count += 1
    tot_list2.append(generated_data)
elapsed_time = time.time() - beginning_time
print(f'Map & appending tuple: {elapsed_time}')

# 10000 range
# NP.Array & appending f string: 6.841000080108643
# Map & appending f string: 6.14900016784668
# NP.Array & appending tuple: 5.888999938964844
# Map & appending tuple: 5.955000162124634

# 100000 range
# NP.Array & appending f string: 65.96399998664856
# Map & appending f string: 63.82099986076355
# NP.Array & appending tuple: 64.62800002098083
# Map & appending tuple: 61.69300031661987




# 10000
# NP.Array & appending f string: 2.021329402923584
# Map & appending f string: 2.0142064094543457
# NP.Array & appending tuple: 1.9465878009796143
# Map & appending tuple: 1.9012455940246582

# NP.Array & appending f string: 19.8583474159240723
# Map & appending f string: 19.601406574249268
# NP.Array & appending tuple: 19.74892258644104
# Map & appending tuple: 19.705182790756226