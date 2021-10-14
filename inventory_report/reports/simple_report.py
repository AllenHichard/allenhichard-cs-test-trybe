import pandas as pd
from datetime import datetime

class SimpleReport:
    
    '''
    Este método recebe dados numa lista contendo estruturas do tipo dict 
    e deverá retornar uma string formatada como um relatório.
    '''
    
    @staticmethod
    def generate(stock):
        df = pd.DataFrame(stock)
        df["data_de_validade"] = pd.to_datetime(df["data_de_validade"])
        oldestManufactureDate = df["data_de_fabricacao"].min()
        closestValidityDate = df.loc[df["data_de_validade"] >= datetime.today()]["data_de_validade"].min().strftime('%Y-%m-%d') 
        companyWithMoreProducts = df['nome_da_empresa'].value_counts().index[0] 
        
        return (f"Data de fabricação mais antiga: {oldestManufactureDate}\n"
               f"Data de validade mais próxima: {closestValidityDate}\n"
               f"Empresa com maior quantidade de produtos estocados: {companyWithMoreProducts}\n")
    

        
