import pandas as pd
import sys
import time


sys.path.append(r'N:\Python220\lesson06\Lesson06\assignment\data')


import cProfile
listtest = []

def do_cprofile(func):

    def profiled_func(*args, **kwargs):
        profile = cProfile.Profile()
        try:
            profile.enable()
            result = func(*args, **kwargs)
            profile.disable()
            return result
        finally:
            print('pandas_perf.py profile:')
            profile.print_stats()
            listtest.append(profile.print_stats())

    return profiled_func

@do_cprofile
def analyze(filename):
    beginning_time = time.time()
    csv_delimiter = ','
    df = pd.read_csv(filename, sep=csv_delimiter)
    data = df.values

    # Analyzer data containers
    year_count = {"2013": 0,
                  "2014": 0,
                  "2015": 0,
                  "2016": 0,
                  "2017": 0,
                  "2018": 0}
    ao_count = 0

    # Iterate through list
    for row in data:
        if 'ao' in row[6]:
            ao_count += 1
            continue
        elif str(row[4]).__contains__('2013'):
            year_count['2013'] += 1
        elif str(row[4]).__contains__('2014'):
            year_count['2014'] += 1
        elif str(row[4]).__contains__('2015'):
            year_count['2015'] += 1
        elif str(row[4]).__contains__('2016'):
            year_count['2016'] += 1
        elif str(row[4]).__contains__('2017'):
            year_count['2017'] += 1
        elif str(row[4]).__contains__('2018'):
            year_count['2018'] += 1


    elapsed_time = time.time()-beginning_time


    # Print results to console
    # print(year_count)
    # print("'ao' was found %s times." % ao_count)
    # print("elapsed time: %s" % elapsed_time)

    return (elapsed_time, year_count, ao_count)




if __name__ == "__main__":

    analyze(r"N:\Python220\lesson06\Lesson06\assignment\data\test.csv")