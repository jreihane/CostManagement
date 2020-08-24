from fileprocessor.CsvPreProcessor import CsvPreProcessor
from fileprocessor.CostProcessor import CostProcessor
from fileprocessor.OsFileProcessor import OsFileProcessor

def manageStatement():
    
    os_file_processor = OsFileProcessor()
    latest_file = os_file_processor.find_latest_statement_file()
    lastest_excel = os_file_processor.find_latest_cost_management_file()
    
    print(latest_file)
    print(lastest_excel)
     
    print("Cleaning CSV file")
    pre_processor = CsvPreProcessor(latest_file)
    pre_processor.clean_sheet()
     
    print("Determining new sheet name")
    cost_list = pre_processor.read_file()
    sheet_name = pre_processor.determine_sheet_name(cost_list[0][0])
     
    print("Processing file")
    cost_processor = CostProcessor(lastest_excel)
    cost_processor.process(cost_list, sheet_name)
         
    print("Finished successfully")

manageStatement()