'''
Created on Aug 24, 2020

@author: reihane
'''
from formatter.AbstractFormatter import AbstractFormatter

class TransportationFormatter(AbstractFormatter):
    '''
    classdocs
    '''
    def get_format(self):
        return super().format("FFC000")

    def get_header(self):
        return ('M', 'Dine out')


    def __init__(self):
        '''
        Constructor
        '''
        