from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports import simple_report, complete_report

class InventoryRefactor (InventoryIterator):

    def __init__(self, importer):
        self.importer = importer
        self.data = []
        
    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, reportType):
        self.data += self.importer.import_data(path)
        exe = {"simples": simple_report.SimpleReport, "completo": complete_report.CompleteReport}
        return exe[reportType].generate(self.data)
        
    
    


