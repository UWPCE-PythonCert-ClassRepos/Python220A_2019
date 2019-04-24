"""
    Learning persistence with Peewee and sqlite
    delete the database to start over
        (but running this program does not require it)

    Person:
        1. insert records
        2. display all records
        3. show transactions
        4. show error checking
        5. show logging (to explain what's going on)

"""
#Note: D. Pokrajac; Technically, this is almost the same as shown on first video, Part 3 (referred to as v3_p1_populate_db.py), 
#except it is not a function

#Corresponds to first in series of files from Lesson 3, Part 3), there, this was implemented as a '
#function "populate_db (starts around 0:45 of video)
from personjob_modeli import * #Used to open a database

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Working with Person class')
logger.info('Note how I use constants and a list of tuples as a simple schema')
logger.info('Normally you probably will have prompted for this from a user')

PERSON_NAME = 0
LIVES_IN_TOWN = 1
NICKNAME = 2

people = [
    ('Andrew', 'Sumner', 'Andy'),
    ('Peter', 'Seattle', None),
    ('Susan', 'Boston', 'Beannie'),
    ('Pam', 'Coventry', 'PJ'),
    ('Steven', 'Colchester', None),
    ]

logger.info('Creating Person records: iterate through the list of tuples')
logger.info('Prepare to explain any errors with exceptions')
logger.info('and the transaction tells the database to rollback on error')

for person in people:
    try:
        with database.transaction(): #Created transaction, and each record is created within a transaction
            new_person = Person.create(
                    person_name = person[PERSON_NAME],
                    lives_in_town = person[LIVES_IN_TOWN],
                    nickname = person[NICKNAME]) #Record created
            new_person.save() #Record saved
            logger.info('Database add successful')

    except Exception as e:
        logger.info(f'Error creating = {person[PERSON_NAME]}')
        logger.info(e)
        logger.info('See how the database protects our data')

logger.info('Read and print all Person records we created...')

for person in Person: #Printing content from a table
    logger.info(f'{person.person_name} lives in {person.lives_in_town} ' +\
        f'and likes to be known as {person.nickname}')

database.close() #Closing database
