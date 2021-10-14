from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as et


class XmlImporter(Importer):

    @staticmethod
    def import_data(path):
        try:
            stock = []
            xml_data = open(path, 'r').read()
            root = et.XML(xml_data)
            cols = ["id", "nome_do_produto", "nome_da_empresa",
                    "data_de_fabricacao", "data_de_validade",
                    "numero_de_serie", "instrucoes_de_armazenamento"]
            for i, child in enumerate(root):
                dict = {}
                for col, subchild in zip(cols, child):
                    dict[col] = subchild.text
                stock.append(dict)
            return stock
        except Exception:
            raise ValueError("Arquivo inválido")
