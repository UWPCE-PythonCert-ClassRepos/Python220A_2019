"""
generate 1 million csv lines following proper schema
"""

import csv
import uuid
from faker import Faker
fake = Faker()


def generate_csv_lines(input_file):
    with open(input_file, 'w') as csv_file:
        writer = csv.DictWriter(csv_file,
                                lineterminator='\n',
                                fieldnames=["seq",
                                            "guid",
                                            "seq",
                                            "seq",
                                            "ccnumber",
                                            "date",
                                            "sentence"])
        writer.writeheader()
        for new_lines in range(1000000):
            writer.writerow(dict(
                seq=new_lines + 1,
                guid=uuid.uuid4(),
                ccnumber=fake.credit_card_number(),
                date=fake.date(pattern="%m/%d/%Y"),
                sentence=fake.sentence()
            ))


if __name__ == "__main__":
    generate_csv_lines(r"C:\Python220\Python220A_2019\students\kevin_cavanaugh\lesson06\assignment\data\exercise.csv")
