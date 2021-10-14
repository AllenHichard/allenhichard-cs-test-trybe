import pandas as pd

from inventory_report.inventory.inventory import Inventory
from inventory_report.inventory.inventory_iterator import InventoryIterator

class InventoryRefactor (InventoryIterator):

    def __init__(self, importer):
        self.importer = importer
        self.data = []
        
    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, reportType):
        self.data += self.importer.import_data(path)
        
    
    


