import pandas as pd
from inventory_report.reports import simple_report, complete_report
import xml.etree.ElementTree as et 


class Inventory:
    
    '''
    Este método capaz de ler um arquivo CSV, JSOM ou XML o qual o 
    caminho é passado como parâmetro
    junto com o tipo de relatório (Simples ou Completo). 
    De acordo com os parâmetros recebidos, 
    deve recuperar os dados do arquivo e chamar o método 
    de gerar relatório correspondente à 
    entrada passada
    Observação: os requisitos: 3, 4 e 5 são similares, 
    mudando apenas a extensão do arquivo.
    '''
    
    @staticmethod
    def import_data(path, reportType):
        if path.endswith('.csv'):
            file = pd.read_csv(path)
        elif path.endswith('.json'):
            file = pd.read_json(path)
        else:
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
            file = pd.DataFrame(stock)
        exe = {"simples": simple_report.SimpleReport, 
               "completo": complete_report.CompleteReport}
        return exe[reportType].generate(file)
