import pandas as pd
from datetime import datetime
from itertools import groupby

class CompleteReport:
    '''
    Este método recebe dados numa lista contendo estruturas do tipo dict 
    e deverá retornar uma string formatada como um relatório.
    '''

    @staticmethod
    def generate(stock):
        df = pd.DataFrame(stock)
        df["data_de_validade"] = pd.to_datetime(df["data_de_validade"])
        oldestManufactureDate = df["data_de_fabricacao"].min()
        closestValidityDate = df.loc[df["data_de_validade"] >= datetime.today()]["data_de_validade"].min().strftime(
            '%Y-%m-%d')
        companyWithMoreProducts = df['nome_da_empresa'].value_counts().index[0]
        return (f"Data de fabricação mais antiga: {oldestManufactureDate}\n"
                f"Data de validade mais próxima: {closestValidityDate}\n"
                f"Empresa com maior quantidade de produtos estocados: {companyWithMoreProducts}\n\n"
                f"Produtos estocados por empresa: \n"
                f"{CompleteReport.listProductsStockedByCompany(df)}")

    @staticmethod
    def listProductsStockedByCompany(df):
        companies = df['nome_da_empresa'].values.tolist()
        dictProductsStockedByCompany = {}
        for company in companies:
            if not company in dictProductsStockedByCompany: 
                dictProductsStockedByCompany[company] = companies.count(company)
        productsStockedByCompany = ""
        for key in dictProductsStockedByCompany:
            productsStockedByCompany += f"- {key}: {dictProductsStockedByCompany[key]}\n"
        return productsStockedByCompany
