'''
Created on Aug 24, 2020

@author: reihane
'''

from openpyxl.styles import Alignment, Font


class AbstractFormatter(object):
    '''
    classdocs
    '''
    
    def format(self, row_color):
        alignment = Alignment(horizontal='center',vertical='bottom',text_rotation=0,wrap_text=False,shrink_to_fit=True,indent=0)
        ft = Font(color= row_color)
        return (alignment, ft)

    def get_format(self):
        return
    
    def get_header(self):
        return

    def __init__(self):
        '''
        Constructor
        '''
        