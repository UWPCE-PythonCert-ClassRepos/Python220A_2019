"""
#----------------------------- #
# Title: poor_perf_1
# Desc: Revisions to poor_perf.py
# Change Log: (Who, When, What)
KCreek, 5/11/2019,
# ----------------------------- #
"""


import datetime
import csv
import logging

# Set Up Logger
logging.basicConfig(level=logging.DEBUG)


def analyze(filename):
    # Starts the Timer
    start = datetime.datetime.now()

    # With loop to process the csv file
    with open(filename) as csvfile:
        # Creates a reader object and gives delimeter
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        # Create a new list
        new_ones = []
        found = 0

        # Searching for "AO"
        AO_search_start = datetime.datetime.now()
        for row in reader:
            lrow = list(row)
            if lrow[5] > '00/00/2012':
                new_ones.append((lrow[5], lrow[0]))
            if "ao" in lrow[6]:
                found += 1
        AO_search_end = datetime.datetime.now()
        AO_search_delta = AO_search_end - AO_search_start
        logging.info("AO Search Time Elapsed: {}".format(AO_search_delta))
        print(f"'ao' was found {found} times")

        # Year Counting Process
        year_count_start = datetime.datetime.now()
        year_count = {
            "2013": 0,
            "2014": 0,
            "2015": 0,
            "2016": 0,
            "2017": 0,
            "2018": 0
        }

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

        year_count_end = datetime.datetime.now()
        delta_year_count = year_count_end - year_count_start
        logging.info("Year Count Elapsed: {}". format(delta_year_count))

        print(year_count)

    end = datetime.datetime.now()
    full_delta = end - start
    logging.info("Total Time: {}".format(full_delta))

    return (start, end, year_count, found)


def main():
    #filename = "data/exercise.csv"
    filename = "testfile.csv"
    analyze(filename)


if __name__ == "__main__":
    main()
