import logging
logger = logging.getLogger()

#if len(logger.parent.handlers)==0:
#    logging.basicConfig( level=logging.INFO,handlers=[logging.StreamHandler()])

def subtract_numbers(a=2,b=3):
        """"dummy function to add two numbers"""
        logger.info('running subtract_numbers function')
        logger.info('{},{}'.format(a,b))
        return a-b
