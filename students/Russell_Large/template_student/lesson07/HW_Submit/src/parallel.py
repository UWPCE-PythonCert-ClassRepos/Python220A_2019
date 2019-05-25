import logging
import os
import time
import threading
import test as d


file_handler = logging.FileHandler('mylog.log')
logger = logging.getLogger()
logger.addHandler(file_handler)



def run_parallel():


    logger.info('###################')
    logger.info('##Parallel info####')
    logger.info('###################')


    beginning_time = time.time()

    folder = os.getcwd()
    csvdir = str(folder[:-3] + '\data')

    t1 = threading.Thread(target=d.import_data, args=(csvdir, 'customer'))
    t2 = threading.Thread(target=d.import_data, args=(csvdir, 'product'))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # Processes are spawned by creating a process objext and
    # then calling its start() method.

    elapsed_time = time.time() - beginning_time

    logger.info(f'threading complete. Total execute time: {elapsed_time}')
    print(f'Parallel complete. Total execute time: {elapsed_time}')

    print(t1)

if __name__ == '__main__':

    run_parallel()






