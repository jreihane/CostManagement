'''
Created on Aug 24, 2020

@author: reihane
'''
from formatter.AbstractFormatter import AbstractFormatter

class DineoutFormatter(AbstractFormatter):
    '''
    classdocs
    '''
    def get_format(self):
        return super().format("00B0F0")

    def get_header(self):
        return ('L', 'Dine out')


    def __init__(self):
        '''
        Constructor
        '''
        