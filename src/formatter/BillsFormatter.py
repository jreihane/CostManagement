'''
Created on Aug 24, 2020

@author: reihane
'''
from formatter.AbstractFormatter import AbstractFormatter

class BillsFormatter(AbstractFormatter):
    '''
    classdocs
    '''

    def get_format(self):
        return super().format("833C0C")

    def get_header(self):
        return ('I', 'Bills')

    def __init__(self):
        '''
        Constructor
        '''
        