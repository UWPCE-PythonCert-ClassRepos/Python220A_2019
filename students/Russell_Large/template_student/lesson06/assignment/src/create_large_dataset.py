import string
import random
import time
import sys
import pandas as pd
import numpy as np

sys.path.append(r'<enter csv folder here>')

newcsv = r'<enter csv location here>'

def get_random_date():

    # 07/21/1901

    month = random.randrange(1, 12)
    day = random.randrange(1, 30)
    year = random.randrange(1900, 2019)

    return f'{month}/{day}/{year}'


def ccnum_gen():

    number = random.randrange(1000000000000000, 9999999999999999)

    return number

def guid_section_gen(size, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for n in np.array(range(size)))

def guid_full_gen():

    first = guid_section_gen(8)
    second = guid_section_gen(4)
    third = guid_section_gen(4)
    fourth = guid_section_gen(4)
    fifth = guid_section_gen(8)

    package = f'{first}-{second}-{third}-{fourth}-{fifth}'

    return package

def char_gen(chars=string.ascii_lowercase):

    size = random.randrange(2, 10)

    t = ''.join(random.choice(chars) for n in np.array(range(size)))

    return t

def sentence():
    return ' '.join(char_gen() for x in range(1,13))


#### Create dataset ####

beginning_time = time.time()
tot_list2 = []
for i in np.array(range(1, 1000000)):

    # seq, guid, seq, seq, ccnumber, date, sentence

    generated_data = count, guid_full_gen(), count, count, ccnum_gen(), get_random_date(), sentence()
    tot_list2.append(generated_data)
    
elapsed_time = time.time() - beginning_time

#### Add data to csv ####

df = pd.DataFrame(tot_list2)
df.to_csv(newcsv, index=False)
