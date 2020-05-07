# This is the dummy application's main function.
# Testing the logging functionality from out here

from qlogger import qlogger
import logging

qlogger.set_display_level('INFO')
qlogger.set_log_file('temp.log')
qlogger.set_rotating_log('PIQ+.log')

logger = qlogger.logger

logger.info('running main.py')


from dosomething import dosomething
ds = dosomething()
ds.add_numbers(2,3)

#qlogger.qlogging.log_to_file('/tmp/mylog.log')

#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#logger = logging.getLogger('muse_data_science/image_score/score_individual_images.py')
#logger.info("hello")
