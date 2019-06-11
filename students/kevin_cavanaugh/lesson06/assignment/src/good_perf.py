"""
better performing, better written module

"""

import datetime
import csv
from collections import defaultdict


def import_data_generator(filename):
    """
    generator to import large csv
    """
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            yield row


def analyze(filename):
    """
    analyze giant csv
    """
    start = datetime.datetime.now()
    gen1 = import_data_generator(filename)
    new_ones = ((list(row)[5], list(row)[0]) for row in gen1
                if list(row)[5] > '00/00/2012')

    year_count = defaultdict(int)
    for new in new_ones:
        if new[0][6:] == '2013':
            year_count["2013"] += 1
        elif new[0][6:] == '2014':
            year_count["2014"] += 1
        elif new[0][6:] == '2015':
            year_count["2015"] += 1
        elif new[0][6:] == '2016':
            year_count["2016"] += 1
        elif new[0][6:] == '2017':
            year_count["2017"] += 1
        elif new[0][6:] == '2018':
            year_count["2018"] += 1

    print(year_count)

    gen2 = import_data_generator(filename)

    found = 0
    for line in gen2:
        if "ea" in line[6]:
            found += 1

    print(f"'ea' was found {found} times")
    end = datetime.datetime.now()
    return start, end, year_count, found


def main():
    """
    main
    """
    filename = r'C:\Python220\Python220A_2019\students\kevin_cavanaugh\lesson06\assignment\data\exercise.csv'
    analyze(filename)


if __name__ == "__main__":
    main()
