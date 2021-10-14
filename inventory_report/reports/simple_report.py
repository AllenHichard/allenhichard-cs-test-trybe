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
        hoje = datetime.today()
        field = "data_de_validade"
        closestValidityDate = df.loc[df[field] >= hoje][field].min()
        closestValidityDate = closestValidityDate.strftime('%Y-%m-%d')
        companyWMProducts = df['nome_da_empresa'].value_counts().index[0]
        p1 = f"Data de fabricação mais antiga: {oldestManufactureDate}\n"
        p2 = f"Data de validade mais próxima: {closestValidityDate}\n"
        p3 = f"Empresa com maior quantidade de produtos estocados: " \
             f"{companyWMProducts}\n"
        return p1+p2+p3
