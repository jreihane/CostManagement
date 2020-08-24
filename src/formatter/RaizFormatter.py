'''
Created on Aug 24, 2020

@author: reihane
'''
from formatter.AbstractFormatter import AbstractFormatter

class RaizFormatter(AbstractFormatter):
    '''
    classdocs
    '''
    def get_format(self):
        return super().format("0070C0")

    def get_header(self):
        return ('K', 'Raiz')


    def __init__(self):
        '''
        Constructor
        '''
        