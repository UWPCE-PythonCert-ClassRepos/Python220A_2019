"""
good_perf.py
Rewrote poor_perf.py with some optimizations.
"""
import csv
from datetime import datetime
from faker import Faker

FAKE = Faker()


def generate_data():
    """Generate random data to fill CSV."""
    with open('../data/exercise.csv', 'w') as file:
        for index in range(1, 1000001):
            guid = FAKE.uuid4()
            ccnumber = FAKE.credit_card_number()
            date = FAKE.date(pattern='%m/%d/%Y')
            text = FAKE.text().replace('\n', ' ')
            file.write(
                f"{index},{guid},{index},{index},{ccnumber},{date},{text}\n")


def analyze(filename):
    """Analyze the file and return the occurences of each year after 2012.

    :params filename str: Name of the file to be analyzed.
    :return duration float: Duration of time the script took to run.
    :return year_count dict: Dict count of years 2013-2019 appearing in file.
    :return found int: Int of how many occurences of string `ao` is found.
    """
    start = datetime.now()
    found = 0
    year_count = {
        "2013": 0,
        "2014": 0,
        "2015": 0,
        "2016": 0,
        "2017": 0,
        "2018": 0,
        "2019": 0
    }

    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader)  # skip header line
        for row in reader:
            try:
                year_count[row[5][6:]] += 1
            except KeyError:
                continue

        print(year_count)
        print(f"'ao' was found {found} times")
    end = datetime.now()
    duration = (end - start)
    return (start, end, year_count, found, duration,)


def main():
    """Main program to execute the analyze function"""
    filename = "../data/exercise.csv"
    analyze(filename)

if __name__ == "__main__":
    main()
