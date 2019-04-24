	"""
    Learning persistence with Peewee and sqlite
    delete the database to start over
        (but running this program does not require it)

    Person:

        1. add a new record and delete it

"""
#D.P. roughly corresponds to function add_and_delete, discussed in first video, Lesson 3, Part 3 video starting around 9:57.

from personjob_modeli import *
#Very important: Note that we have to load this module.
#It is not SUFFICIENT to just connect to the database; we also need define the classes corresponding to the tables
#so that we can interface stored data (DP)

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

PERSON_NAME = 0
LIVES_IN_TOWN = 1
NICKNAME = 2

logger.info('Add and display a Person called Fred; then delete him...')

logger.info('Add Fred in one step')

#We've already seen this in part 1, lesson 3.
new_person = Person.create(
    person_name = 'Fred',
    lives_in_town = 'Seattle',
    nickname = 'Fearless')
new_person.save()

#Try to execute this insertion once more. What would happen?]

logger.info('Show Fred')
aperson = Person.get(Person.person_name == 'Fred')
aperson.delete_instance()

logger.info('Reading and print all Person records (but not Fred; he has been deleted)...')

for person in Person:
    logger.info(f'{person.person_name} lives in {person.lives_in_town} and likes to be known as {person.nickname}')

database.close()
