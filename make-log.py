from csv_logger import CsvLogger
import logging
import random
from time import sleep

filename = 'logs/log.csv'
delimiter = ','
level = logging.INFO
custom_additional_levels = ['logs_a', 'logs_b', 'logs_c']
fmt = f'%(asctime)s{delimiter}%(levelname)s{delimiter}%(message)s'
datefmt = '%Y/%m/%d %H:%M:%S'
# datefmt = ''
max_size = 100000000  # big
max_files = 4  # 4 rotating files
# header = ['ts', 'level', 'value_1', 'value_2']
header = []

# Creat logger with csv rotating handler
csvlogger = CsvLogger(filename=filename,
                      delimiter=delimiter,
                      level=level,
                      add_level_names=custom_additional_levels,
                      add_level_nums=None,
                      fmt=fmt,
                      datefmt=datefmt,
                      max_size=max_size,
                      max_files=max_files,
                      header=header)

while True:

    # Log some records
    for i in range(3):
        csvlogger.logs_a([i, i * 2])
        sleep(3)

    # You can log list or string
    csvlogger.logs_b([1000.1, 2000.2])
    sleep(3)
    csvlogger.critical('3000,4000')
    sleep(3)

    # Log some more
    for i in range(5):
        csvlogger.logs_c([random.randint(i,i+5), float(random.randint(i,i+5)**2)])
        sleep(3)

# Read and print all of the logs from file after logging
# all_logs = csvlogger.get_logs(evaluate=False)
# for log in all_logs:
#    print(log)
