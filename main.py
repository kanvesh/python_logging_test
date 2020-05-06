from qlogger import qlogger

qlogger.set_level_display('INFO')
qlogger.set_log_file('temp.log')
qlogger.create_timed_rotating_log('PIQ+')
logger = qlogger.logger

logger.info('running main.py')


from dosomething import dosomething
ds = dosomething()
ds.add_numbers(2,3)
