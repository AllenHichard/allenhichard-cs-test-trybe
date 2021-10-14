import pandas as pd
from datetime import datetime


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
        field = "data_de_validade"
        closestValidDate = df.loc[df[field] >= datetime.today()][field].min()
        closestValidityDate = closestValidDate.strftime('%Y-%m-%d')
        companyMProducts = df['nome_da_empresa'].value_counts().index[0]
        return (f"Data de fabricação mais antiga: "
                f"{oldestManufactureDate}\n"
                f"Data de validade mais próxima: "
                f"{closestValidityDate}\n"
                f"Empresa com maior quantidade de produtos estocados: "
                f"{companyMProducts}\n\n"
                f"Produtos estocados por empresa: \n"
                f"{CompleteReport.listProductsStockedCompany(df)}")

    @staticmethod
    def listProductsStockedCompany(df):
        companies = df['nome_da_empresa'].values.tolist()
        dictProductsStockedCompany = {}
        for company in companies:
            if company not in dictProductsStockedCompany:
                dictProductsStockedCompany[company] = companies.count(company)
        StockedCompany = ""
        for key in dictProductsStockedCompany:
            StockedCompany += f"- {key}: {dictProductsStockedCompany[key]}\n"
        return StockedCompany
