'''
Created on Aug 24, 2020

@author: reihane
'''
from formatter.AbstractFormatter import AbstractFormatter

class OthersFormatter(AbstractFormatter):
    '''
    classdocs
    '''
    def get_format(self):
        return super().format("BF8F00")

    def get_header(self):
        return ('J', 'Others')


    def __init__(self):
        '''
        Constructor
        '''
        