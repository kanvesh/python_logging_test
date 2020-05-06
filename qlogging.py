import logging

# Create a custom logger
class qlogging():

    def __init__(self, process_name=__name__):

        """Initiate the Quotient logging module
        Add a default handler that prints to stdout"""

        self.logger = logging.getLogger(process_name)
        self.logger.setLevel(logging.DEBUG)

        # Create handlers
        c_handler = logging.StreamHandler()
        c_handler.setLevel(logging.DEBUG)

        # Create formatters and add it to handlers
        self.stdout_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(self.stdout_format)

        # Add handlers to the logger
        self.logger.addHandler(c_handler)

        return None

    def set_log_file(self, filename, loglevel = logging.DEBUG, output_format=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')):

        """This function lets you choose a custom file to store the log"""

        f_handler = logging.FileHandler(filename)
        f_handler.setLevel(loglevel)
        f_handler.setFormatter(output_format)
        self.logger.addHandler(f_handler)

        return None
