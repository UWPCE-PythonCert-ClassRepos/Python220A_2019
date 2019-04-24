"""
    Learning persistence with Peewee and sqlite
    delete the database to start over
        (but running this program does not require it)


"""
#
#Corresponds to show_integrity_add() , show_integrity_del(), Video 2, Part 3, Lesson 3
#Starting from 12~13
#
#Referred at ~12:13 Video 2, Part 3, Lesson 3, corresponding to show_integrity_add() function there

from personjob_modeli import *

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Try to add a new job where a person doesnt exist...')

addjob = ('Sales', '2010-04-01', '2018-02-08', 80400, 'Harry')

logger.info('Adding a sales job for Harry')
logger.info(addjob)

try:
    with database.transaction():
        new_job = Job.create(
                job_name = addjob[JOB_NAME],
                start_date = addjob[START_DATE],
                end_date = addjob[END_DATE],
                salary = addjob[SALARY],
                person_employed = addjob[PERSON_EMPLOYED])
        new_job.save()

except Exception as e:
    logger.info('Add failed because Harry is not in Person')
    logger.info(f'For Job create: {addjob[0]}')
    logger.info(e)

#This corresponds to show_integrity_del ~14:20, Video 2, Part 3, lesson 3
logger.info('Try to Delete a person who has jobs...')


try:
    with database.transaction():
        aperson = Person.get(Person.person_name == 'Andrew')
        logger.info(f'Trying to delete {aperson.person_name} who lives in {aperson.lives_in_town}')
        aperson.delete_instance()

except Exception as e:
    logger.info('Delete failed because Andrew has Jobs')
    logger.info(f'Delete failed: {aperson.person_name}')
    logger.info(e)

database.close()
