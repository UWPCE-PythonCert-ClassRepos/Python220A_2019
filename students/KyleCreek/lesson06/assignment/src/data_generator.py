"""
#----------------------------- #
# Title: data_generator.py
# Desc: Revisions to poor_perf.py
# Change Log: (Who, When, What)
KCreek, 5/10/2019, Wrote Script
KCreek, 5/14/2019, Cleaned Script
to adhere to pylint standards
# ----------------------------- #
"""
import csv
import datetime
import random
import uuid
from essential_generators import DocumentGenerator


def date_generator():
    """
    Generates a random date in xx/xx/xxxx
    formated
    :return: String of randomized date
    """

    # Create lists of available months, days, years
    months = [i for i in range(1, 13)]
    days = [j for j in range(1, 29)]
    years = [k for k in range(1900, 2019)]

    # Establish random index values to choose from list
    rand_month_index = random.randint(0, len(months)-1)
    rand_day_index = random.randint(0, len(days)-1)
    rand_year_index = random.randint(0, len(years)-1)

    # Generate random months, days, and years
    month = months[rand_month_index]
    day = days[rand_day_index]
    year = years[rand_year_index]

    # Return a string of information containing month, day, and year
    date = '{}/{}/{}'.format(month, day, year)
    return date


def word_maker():
    """
    Function creates random "word" strings
    :return: String of nonsense word
    """

    # List of all letters in the alphabet
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']

    # Establish word Length
    word_length = random.randint(2, 15)

    # fill string with letters
    word = ''
    counter = 0
    while counter < word_length:
        new_letter = alphabet[random.randint(0, 25)]
        word += new_letter
        counter += 1
    return word


def sentence_maker():
    """
    Function creates sentences of non-sense
    :return: String of sentence
    """

    # Determine random sentence length
    sentence_length = random.randint(1, 20)

    # Empty list to store the sentence words
    sentence_words = []

    counter = 0
    while counter < sentence_length:
        sentence_words.append(word_maker())
        counter += 1

    return_sentence = ' '.join(sentence_words)
    return return_sentence


def sentence_generator():
    """
    Utilizes essential_generators to create a random sentence for
    .csv file
    :return: String Containing random sentence.
    """

    # Create an instance of the document generator
    generator = DocumentGenerator()

    return generator.sentence()


def data_generator(data_point):
    """"
    Generates data for .CSV file
    :return: List of Data to write to .csv
    file
    """

    sequence = 0
    data_list = []
    while sequence < data_point:
        date = date_generator()
        sentence = sentence_maker()
        sequence += 1
        guid = str(uuid.uuid1())
        sequence_list = [sequence, guid, sequence,
                         sequence, 'cc', date, sentence]
        data_list.append(sequence_list)
    return data_list


def main():
    """
    Performs the Main functionality of data_generator.py
    :return: Writes .csv file w/ 1 Million Records
    """
    # Writes the files to the .csv
    start = datetime.datetime.now()
    with open('exercise.csv', mode='w', newline='') as testfile:
        test_writer = csv.writer(testfile, delimiter=',', quotechar='"',
                                 quoting=csv.QUOTE_MINIMAL)
        data = data_generator(1000000)
        for row in data:
            test_writer.writerow(row)

    end = datetime.datetime.now()

    delta = end - start
    print("Time Elapsed", delta)


if __name__ == "__main__":
    main()
