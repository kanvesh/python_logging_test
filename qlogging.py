#This is the internal logging class.
#An stderr handler is initiated by default.
#Other methods are provided to customize handlers and formatters


import logging
from logging.handlers import TimedRotatingFileHandler

# Create a custom logger
class qlogging():
    #@abstractmethod
    #def log_to_file(filename):
        #logging = qlogging(filename)

    def __init__(self):

        """Initiate the Quotient logging module
        Add a default handler that prints to stderr"""

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # Create handlers
        c_handler = logging.StreamHandler()
        c_handler.setLevel(logging.DEBUG)

        # Create formatters and add it to handlers
        self.stdout_format = logging.Formatter('%(message)s')
        c_handler.setFormatter(self.stdout_format)

        # Add handlers to the logger
        self.logger.addHandler(c_handler)

        #self.set_log_file(filename)

    def set_log_file(self, filename, loglevel = logging.DEBUG, output_format=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')):

        """This function lets you choose a custom file to store the log"""

        f_handler = logging.FileHandler(filename)
        f_handler.setLevel(loglevel)
        f_handler.setFormatter(output_format)
        self.logger.addHandler(f_handler)

        return None

    def set_display_level(self, level='DEBUG'):

        """This function sets level of stderr that is displayed"""

        level = level.upper()

        if level=='DEBUG':
            loglevel = logging.DEBUG
        elif level=='INFO':
            loglevel = logging.INFO
        elif level=='WARNING':
            loglevel = logging.WARNING
        elif level=='ERROR':
            loglevel = logging.ERROR
        elif level=='CRITICAL':
            loglevel = logging.CRITICAL

        self.logger.handlers[0].setLevel(loglevel)


    def set_rotating_log(self, path='temp.log', period='d', interval=1, output_format=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')):

        """Creates a new log every day by default. Time period is changeable."""

        timed_handler = TimedRotatingFileHandler(path,
                                           when=period,
                                           interval=interval,
                                           backupCount=0)
        timed_handler.setFormatter(output_format)
        self.logger.addHandler(timed_handler)
