#This is a dummy module that is called by the main function
#This inturn calls another dummy module dosomething else

import logging
logger = logging.getLogger()
from dosomethingelse import subtract_numbers

#if len(logger.parent.handlers)==0:
    #logging.basicConfig( level=logging.INFO,handlers=[logging.StreamHandler()])

class dosomething():

    def __init__(self):

        logger.info('initiating dosomething module')

    def add_numbers(self,a=2,b=3):
        """"dummy function to add two numbers"""
        logger.info('running add_numbers function')
        logger.info('{},{}'.format(a,b))
        return subtract_numbers(a,b)
