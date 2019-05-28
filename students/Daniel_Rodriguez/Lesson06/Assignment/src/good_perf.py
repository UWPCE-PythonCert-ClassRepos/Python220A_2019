"""
poorly performing, poorly written module

"""

import datetime
import csv
import timeit


def year_2013():
    """Switch case"""
    return '2013'


def year_2014():
    """Switch case"""
    return '2014'


def year_2015():
    """Switch case"""
    return '2015'


def year_2016():
    """Switch case"""
    return '2016'


def year_2017():
    """Switch case"""
    return '2017'


def year_2018():
    """Switch case"""
    return '2018'


def analyze(filename):
    """Analyses data file"""
    start = datetime.datetime.now()

    with open(filename) as csv_file:
        reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        new_ones = []

        for row in reader:

            if row[5] > '00/00/2012':
                new_ones.append((row[5], row[0]))

        year_count = {
            '2013': 0,
            '2014': 0,
            '2015': 0,
            '2016': 0,
            '2017': 0,
            '2018': 0
        }

        switcher = {
            '2013': year_2013(),
            '2014': year_2014(),
            '2015': year_2015(),
            '2016': year_2016(),
            '2017': year_2017(),
            '2018': year_2018()
        }

        for new in new_ones:
            # print(f'From For Loop: {new[0][6:]}')

            year = switcher.get(new[0][6:])
            # print(f'From Dictionary: {year}, {type(year)}')
            try:
                year_count[year] += 1
            except KeyError as e:
                pass

        print(year_count)

        found = 0
        for line in reader:
            if 'ao' in line[6]:
                found += 1

        print(f"'ao' was found {found} times")
        end = datetime.datetime.now()

    return start, end, year_count, found


def main():
    """Main function"""
    filename = '../data/exercise - 1000000.csv'
    analyze(filename)


if __name__ == '__main__':
    print(timeit.timeit('main()', 'from __main__ import main', number=1))
