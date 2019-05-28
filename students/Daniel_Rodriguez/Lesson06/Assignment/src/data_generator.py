# ---------------------------------------------------------------------------- #
# Course: PYTHON 220: Advanced Programming in Python
# Script Title: Exercise Data Generator
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-05-27, Initial release
# ---------------------------------------------------------------------------- #

import csv
import logging
import uuid

from faker import Faker
fake = Faker()
uuid.uuid4()

logging.basicConfig(level=logging.DEBUG)

FILE_PATH = '../data/exercise.csv'
# logging.debug('Data file path: {}'.format(FILE_PATH))

FILE_HEADERS = ['seq', 'guid', 'seq', 'seq', 'ccnumber', 'date', 'sentence']

with open(FILE_PATH, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(FILE_HEADERS)

    for x in range(1000):
        seq = x + 1
        guid = str(uuid.uuid4())
        cc_number = fake.credit_card_number()
        date = fake.date(pattern="%m/%d/%Y", end_datetime=None)
        sentence = fake.sentence(nb_words=10, variable_nb_words=True)
        csv_data = [seq, guid, seq, seq, cc_number, date, sentence]

        writer.writerow(csv_data)
