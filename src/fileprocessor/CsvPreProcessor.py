'''
Created on Aug 25, 2020

@author: reihane
'''
import csv
import os
from datetime import datetime

class CsvPreProcessor(object):
    '''
    classdocs
    '''
    
    def clean_sheet(self):
        temp_file_name = self.csv_file + "_"
        
        with open(self.csv_file, 'rt') as inp, open(temp_file_name, 'wt', newline='') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                if(len(row) > 1):
                    if (float(row[1].strip('"')) < 0 and (row[2].find('017318314994597') == -1 and row[2].find('ACCOUNT SERVICING FEE') == -1)):
                        writer.writerow(row)
        
        os.remove(self.csv_file, dir_fd=None)
        os.rename(temp_file_name, self.csv_file, src_dir_fd=None, dst_dir_fd=None)
     

    def determine_sheet_name(self, first_cell_value):
        cost_date = datetime.strptime(first_cell_value.strip('"'), '%d/%m/%Y')
        
        return cost_date.strftime("%B") + "-" + cost_date.strftime("%G")


    def read_file(self):
        with open(self.csv_file, newline='') as csvfile:
            costs_list = list(csv.reader(csvfile, delimiter=',', quotechar='|'))
        
        return costs_list

 
    def __init__(self, csv_file):
        '''
        Constructor
        '''
        self.csv_file = csv_file
        