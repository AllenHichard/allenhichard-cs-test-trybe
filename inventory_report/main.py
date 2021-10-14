from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor
import sys


def main():
    if len(sys.argv) < 3:
        sys.stderr.write("Verifique os argumentos\n")
    else:
        id, path, reportType = sys.argv
        extension = path.split(".")[1]
        importers = {"csv": InventoryRefactor(CsvImporter), 
                     "json": InventoryRefactor(JsonImporter), 
                     "xml": InventoryRefactor(XmlImporter)}
        instance = importers[extension]
        sys.stdout.write(instance.import_data(path, reportType))
