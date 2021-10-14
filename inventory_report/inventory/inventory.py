import pandas as pd
from inventory_report.reports import simple_report, complete_report

class Inventory:
    
    
    '''
    Este método capaz de ler um arquivo CSV, JSOM ou XML o qual o caminho é passado como parâmetro
    junto com o tipo de relatório (Simples ou Completo). De acordo com os parâmetros recebidos, 
    deve recuperar os dados do arquivo e chamar o método de gerar relatório correspondente à 
    entrada passada
    Observação: os requisitos: 3, 4 e 5 são similares, mudando apenas a extensão do arquivo.
    '''
    
    
    @staticmethod
    def import_data(path, reportType):
        if path.endswith('.csv'):
            file = pd.read_csv("../"+path)
        elif path.endswith('.json'):
            file = pd.read_json("../" + path)
        else:
            file = pd.read_xml("../" + path)
        exe = {"simples": simple_report.SimpleReport, "completo": complete_report.CompleteReport}
        return exe[reportType].generate(file)
    
    
        
