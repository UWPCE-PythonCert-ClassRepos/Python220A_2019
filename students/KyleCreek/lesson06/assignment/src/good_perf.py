"""
#----------------------------- #
# Title: good_perf.py
# Desc: Revisions to poor_perf.py
# Change Log: (Who, When, What)
KCreek, 5/14/2018, Finalized Script
# ----------------------------- #
"""

import csv
import datetime
import logging

# Set Up Logger
logging.basicConfig(level=logging.DEBUG)


def analyze(filename):
    """
    Function analyzes .csv File with 1 million records
    :param filename: String of File Name
    :return: Tuple Containing Various Data
    """
    # Establish Analysis Timer
    start = datetime.datetime.now()

    # With Loop to Process csv File
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')

        # Establish list to store data and counter for
        # number of times "AO" is found
        new_ones = []
        found = 0

        # Interrogate each row in the csv object
        for row in reader:
            lrow = list(row)
            if lrow[5] > '00/00/2012':
                new_ones.append((lrow[5], lrow[0]))
            if "ao" in lrow[6]:
                found += 1
        print(f"'ao' was found {found} times")

        # Establish dictionary to contain the years counted
        year_count = {
            "2013": 0,
            "2014": 0,
            "2015": 0,
            "2016": 0,
            "2017": 0,
            "2018": 0
        }

        # 'for' loop interrogates data and adds to dictionary
        # when instances are found
        for new in new_ones:
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

        print(year_count)

    end = datetime.datetime.now()
    full_delta = end - start
    logging.info("Total Time: {}".format(full_delta))

    return start, end, year_count, found


def main():
    """
    Runs the main loop function of "good_perf.py"
    :return: None
    """
    filename = "exercise.csv"
    analyze(filename)


if __name__ == "__main__":
    main()
