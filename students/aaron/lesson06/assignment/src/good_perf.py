"""
great performing, greatly written module

"""

import datetime
import random
from faker import Faker
import csv
import os
from string import ascii_lowercase, digits

def gen_data(filename, entries, regenerate = False):
    ''' Generates a ton of random entries and dumps them into filename '''
    if os.path.isfile(filename) and regenerate == False:
        # dont regenerate data if the file exists
        return
    print("Generating data in %s" % filename)
    f = open(filename, 'w+')
    f.write("seq,guid,seq,seq,ccnumber,date,sequence\n")
    fakerer = Faker()
    word_list = ["karaoke", "test", "words", "stuff", "apple", "orange",
                 "fedora", "list", "canary", "slugs", "snails", "flipper",
                 "sandals", "shoes", "nails", "hammers", "to", "the", "and",
                 "asdfsadjf", "asdf", "noise", "random", "letters"]
    for row in range(entries):
        data = "%s,%s,%s,%s,%s,%s,%s\n" % (row, fakerer.uuid4(), row, row,
                   fakerer.credit_card_number(),
                   fakerer.date(pattern="%m/%d/%Y"),
                   fakerer.text(ext_word_list=word_list).replace('\n', ' ').replace(',', ' '))
        f.write(data)
    f.close()
    print("Generated data.")


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
    ''' the main function automatically loads data/generated_data.csv '''
    ''' if the file doesn't exist already '''
    filename = "data/generated_data.csv"
    analyze(filename)


if __name__ == "__main__":
    main()
