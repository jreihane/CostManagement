'''
Created on Aug 25, 2020

@author: reihane
'''
from fileprocessor.ExcelProcessor import ExcelProcessor
from formatter.FormatFactory import FormatFactory

class CostProcessor(object):
    '''
    classdocs
    '''
    def process(self, costs_list, sheet_name):
        
        self.excel_processor.create_sheet(sheet_name)     
        self._calculate_and_write(costs_list)
        self.excel_processor.clean_worksheet()
        
        self.excel_processor.save_workbook()
    
                             
    def _calculate_and_write(self, costs_list):
        for row_num, row in enumerate(costs_list):
            if(len(row) > 1):
                amount = float(row[1].strip('"'))
                if(amount < 0):
                    desc = row[2]
                    
                    try:
                        row_formatter = self.formatFactory.get_formatter(desc)
                        row_header = self.formatFactory.get_header(desc)
                        
                        self.excel_processor.insert_row(row_num+1, row)
                        
                        self.excel_processor.format_row(row_num+1, row_formatter)
                        new_value = self.sum_total_for_category(row[1], row_header)
                        self.excel_processor.update_total_cell(row_header, new_value)
                        self.excel_processor.format_cells(row_formatter, row_header)
                    except:
                        print("Exception!" + str(row_num) + " " + desc)

    
    def sum_total_for_category(self, row_value, row_header):
        current_value = self.excel_processor.get_current_cell_value(row_header[0])
        if(current_value == "None"):
            current_value = "0"
            
        return (float(row_value.strip('"')) + float(current_value.strip('"'))) 
        

    def __init__(self, excel_path):
        '''
        Constructor
        '''
        self.excel_path = excel_path
        self.excel_processor = ExcelProcessor(self.excel_path)
        self.formatFactory = FormatFactory()