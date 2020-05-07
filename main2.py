# This is the another dummy application's main function.
# Testing to see the functionality works if run in parallel

from qlogger import qlogger

qlogger.set_display_level('DEBUG')
qlogger.set_log_file('temp.log')
qlogger.set_rotating_log('PIQ+.log')
logger = qlogger.logger

logger.info('running main.py')


from dosomething import dosomething
ds = dosomething()
ds.add_numbers(2,3)
