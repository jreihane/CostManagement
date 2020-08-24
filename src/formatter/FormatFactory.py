from formatter.AccomodationFormatter import AccomodationFormatter
from formatter.RaizFormatter import RaizFormatter
from formatter.BillsFormatter import BillsFormatter
from formatter.TransportationFormatter import TransportationFormatter
from formatter.GroceryFormatter import GroceryFormatter
from formatter.DineoutFormatter import DineoutFormatter
from formatter.DonationsFormatter import DonationsFormatter
from formatter.OthersFormatter import OthersFormatter


class FormatFactory:
    def _get_formatter_class(self, desc):
        if (desc.find('PMM') > -1):
            return AccomodationFormatter()
        
        elif (desc.find('RAIZ') > -1):
            return (RaizFormatter())
            
        elif (desc.find('AURORA') > -1 or desc.find('NETFLIX') > -1 or desc.find('TELSTRA') > -1 or desc.find('RACT') > -1):
            return (BillsFormatter())
        
        elif (desc.find('CALTEX') > -1):
            return (TransportationFormatter())
            
        elif (desc.find('COLES') > -1 or desc.find('WOOLWORTH') > -1):
            return (GroceryFormatter())
            
        elif (desc.find('MCDONALD') > -1 or desc.find('NANDO') > -1 or desc.find('PIZZA') > -1):
            return (DineoutFormatter())
            
        elif (desc.find('CEREBRAL PALSY') > -1 or desc.find('WORLD ANIMAL PROTECTION') > -1 or desc.find('UNHCR') > -1):
            return (DonationsFormatter())
            
        else:
            if(desc.find('017318314994597') == -1 and desc.find('ACCOUNT SERVICING FEE') == -1):
                return (OthersFormatter())
            
    def get_formatter(self, desc):
        formatter = self._get_formatter_class(desc)
        return formatter.get_format()
            
    def get_header(self, desc):
        formatter = self._get_formatter_class(desc)
        return formatter.get_header()
            
    