from qlogger import qlogger

qlogger.set_level_display('WARNING')
#qlogger.set_log_file('temp.log')
logger = qlogger.logger

logger.info('running main.py')


from dosomething import dosomething
ds = dosomething()
ds.add_numbers(2,3)
