"""
poorly performing, poorly written module

"""

import datetime
import csv

def analyze(filename):
    ''' checks filename for specific years and 'ao' in column 6 '''
    start = datetime.datetime.now()
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')

        year_count = {
            "2013": 0,
            "2014": 0,
            "2015": 0,
            "2016": 0,
            "2017": 0,
            "2018": 0
        }
        found = 0

        for row in reader:
            lrow = list(row)

            try:
                year = int(lrow[5][6:])
            except ValueError:
                continue
            if 2012 < year <= 2018:
                year_count[str(year)] += 1
            if "ao" in lrow[6]:
                found += 1

        print(year_count)
        print(f"'ao' was found {found} times")
        end = datetime.datetime.now()
    return (start, end, year_count, found)

def main():
    ''' the main function automatically loads data/exercise.csv '''
    filename = "data/exercise.csv"
    analyze(filename)


if __name__ == "__main__":
    main()
