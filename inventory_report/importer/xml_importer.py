from inventory_report.importer.importer import Importer
import pandas as pd

class XmlImporter(Importer):

    @staticmethod
    def import_data(path):
        try:
            file = pd.read_xml(path)
            stock = []
            for item in file.iterrows():  # name=None
                item[1]["id"] = str(item[1]["id"])
                stock.append(dict(item[1]))
            return stock
        except:
            raise ValueError("Arquivo inválido")
