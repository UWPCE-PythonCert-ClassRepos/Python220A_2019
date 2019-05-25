import logging
import os
import sys
import time
from multiprocessing import Process
import test as d


file_handler = logging.FileHandler('mylog.log')
logger = logging.getLogger()
logger.addHandler(file_handler)


if __name__ == '__main__':

    logger.info('###################')
    logger.info('####Linear info####')
    logger.info('###################')

    beginning_time = time.time()

    folder = os.getcwd()
    csvdir = str(folder[:-3] + '\data')

    processes = []

    files = ['customer', 'product', 'rental']

    for file in files:
        process = Process(target=d.import_data, args=(csvdir, file))
        processes.append(process)

        # Processes are spawned by creating a process objext and
        # then calling its start() method.
        process.start()

    for process in processes:
        process.join()

    elapsed_time = time.time() - beginning_time

    logger.info(f'Linear complete. Total execute time: {elapsed_time}')
    # print(f'multip complete. Total execute time: {elapsed_time}')






