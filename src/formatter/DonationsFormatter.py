'''
Created on Aug 24, 2020

@author: reihane
'''
from formatter.AbstractFormatter import AbstractFormatter

class DonationsFormatter(AbstractFormatter):
    '''
    classdocs
    '''
    def get_format(self):
        return super().format("96992F")

    def get_header(self):
        return ('H', 'Donations')


    def __init__(self):
        '''
        Constructor
        '''
        