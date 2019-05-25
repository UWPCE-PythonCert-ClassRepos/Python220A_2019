import logging
import os
import time
import test as d


file_handler = logging.FileHandler('mylog.log')
logger = logging.getLogger()
logger.addHandler(file_handler)

logger.info('###################')
logger.info('###Regular info####')
logger.info('###################')

# add into import
folder = os.getcwd()
csvdir = str(folder[:-3] + '\data')


file_handler = logging.FileHandler('mylog.log')
logger = logging.getLogger()
logger.addHandler(file_handler)

beginning_time = time.time()

files = ['customer', 'product']

for file in files:
    filelocation = r'{}\\{}.csv'.format(csvdir, file)
    d.import_data(csvdir, file)

elapsed_time = time.time() - beginning_time

logger.info(f'normal run complete. Total execute time: {elapsed_time}')
