'''
Created on Aug 24, 2020

@author: reihane
'''
from formatter.AbstractFormatter import AbstractFormatter

class GroceryFormatter(AbstractFormatter):
    '''
    classdocs
    '''
    def get_format(self):
        return super().format("000000")

    def get_header(self):
        return ('F', 'Grocery')


    def __init__(self):
        '''
        Constructor
        '''
        