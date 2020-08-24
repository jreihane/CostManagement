'''
Created on Aug 24, 2020

@author: reihane
'''
from formatter.AbstractFormatter import AbstractFormatter

class AccomodationFormatter(AbstractFormatter):
    '''
    classdocs
    '''
    
    def get_format(self):
        return super().format("B513AD")

    def get_header(self):
        return ('G', 'Rent')

    def __init__(self):
        '''
        Constructor
        '''
        