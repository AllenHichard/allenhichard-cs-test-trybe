from inventory_report.importer.importer import Importer
import pandas as pd
class JsonImporter(Importer):

    @staticmethod
    def import_data(path):
        try:
            file = pd.read_json("../" + path)
            LIST = []
            for tuple in file.iterrows():  # name=None
                tuple[1]["id"] = str(tuple[1]["id"])
                LIST.append(dict(tuple[1]))
            return LIST
        except:
            raise ValueError("Arquivo inválido")
