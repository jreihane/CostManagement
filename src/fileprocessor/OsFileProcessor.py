'''
Created on Aug 25, 2020

@author: reihane
'''
import os

class OsFileProcessor(object):
    '''
    classdocs
    '''
    def find_latest_statement_file(self):
        max_mtime = 0
        for dirname,subdirs,files in os.walk("C:/Users/reihane/Downloads/"):
            for fname in files:
                if(fname.find("ANZ") != -1):
                    full_path = os.path.join(dirname, fname)
                    mtime = os.stat(full_path).st_mtime
                    if mtime > max_mtime:
                        max_mtime = mtime
                        max_dir = dirname
                        max_file = fname

        return (max_dir + max_file)


    def find_latest_cost_management_file(self):
        for dirname,subdirs,files in os.walk("C:/Users/reihane/Desktop/"):
            for fname in files:
                if(fname.find("CostManagement") != -1):
                    return (dirname + fname)


    def __init__(self):
        '''
        Constructor
        '''
        