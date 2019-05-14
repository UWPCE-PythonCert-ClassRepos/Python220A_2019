"""
poorly performing, poorly written module

"""

import datetime
import csv
import logging

# Set Up Logger
logging.basicConfig(level=logging.DEBUG)


def analyze(filename):
    # Starts the Timer
    start = datetime.datetime.now()

    csv_start = datetime.datetime.now()
    # Create a .CSV File
    csvfile = open(filename, 'r')

    # Create a reader object
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')

    csv_end = datetime.datetime.now()

    csv_delta = csv_end - csv_start
    logging.info("CSV Reader Time {}". format(csv_delta))

    AO_search_start = datetime.datetime.now()
    # Create Empty List and  found
    new_ones = []
    found = 0

    # Populate New Ones and Determine Number of times "AO" is found
    for row in reader:
        lrow = list(row)
        if lrow[5] > '00/00/2012':
            new_ones.append((lrow[5], lrow[0]))
            new_ones.append((lrow[5], lrow[0]))
        if "ao" in lrow[6]:
            found += 1
    print(f"'ao' was found {found} times")
    AO_search_end = datetime.datetime.now()

    AO_delta = AO_search_end - AO_search_start
    logging.info("AO Search Time Elapsed: {}".format(AO_delta))

    new_ones_start = datetime.datetime.now()
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

    new_ones_end = datetime.datetime.now()
    delta_new_ones = new_ones_end - new_ones_start
    logging.info("New Ones Elapsed: {}". format(delta_new_ones))

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
