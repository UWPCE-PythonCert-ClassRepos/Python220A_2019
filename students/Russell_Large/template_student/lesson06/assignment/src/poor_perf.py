"""
poorly performing, poorly written module

"""

import time
import csv
import sys
import cProfile

sys.path.append(r'N:\Python220\lesson06\Lesson06\assignment\data')


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
            print('poor_perf.py profile:')
            profile.print_stats()
            listtest.append(profile.print_stats())

    return profiled_func

@do_cprofile
def analyze(filename):
    beginning_time = time.time()
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        new_ones = []
        for row in reader:
            lrow = list(row)
            if lrow[5] > '00/00/2012':
                new_ones.append((lrow[5], lrow[0]))

        year_count = {
            "2013": 0,
            "2014": 0,
            "2015": 0,
            "2016": 0,
            "2017": 0,
            "2018": 0
        }

        for new in new_ones:
            # print(new[0][5:])
            if new[0][6:] == '2013':
                year_count["2013"] += 1
            if new[0][6:] == '2014':
                year_count["2014"] += 1
            if new[0][6:] == '2015':
                year_count["2015"] += 1
            if new[0][6:] == '2016':
                year_count["2016"] += 1
            if new[0][6:] == '2017':
                year_count["2017"] += 1
            if new[0][6:] == '2018':
                year_count["2017"] += 1

        # print(year_count)

    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')

        found = 0

        for line in reader:
            lrow = list(line)
            if "ao" in line[6]:
                found += 1

        # print(f"'ao' was found {found} times")

        elapsed_time = time.time() - beginning_time

        # print(elapsed_time)

    return (elapsed_time, year_count, found)

def main():
    filename = r"N:\Python220\lesson06\Lesson06\assignment\data\test.csv"
    analyze(filename)


if __name__ == "__main__":
    main()
