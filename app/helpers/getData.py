from zipfile import ZipFile
from bs4 import BeautifulSoup
import pandas as pd
import requests
import pathlib
import os


def obtainData():

    # We obtain the main directory of the program
    rootDir = pathlib.Path.cwd()

    # We obtain the directory where the data will be downloaded
    resourcesDir = rootDir.joinpath('resources')

    databasePath = resourcesDir.joinpath('DadosMegasena.html')

    # Website of the archive with the data
    url = "http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbwMPI0sDBxNXAOMwrzCjA0sjIEKIoEKnN0dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wNnUwNHfxcnSwBgIDUyhCvA5EawAjxsKckMjDDI9FQE-F4ca/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0K8DBC0QPVN93KQ10G1/res/id=historicoHTML/c=cacheLevelPage/=/"

    try:
        # Object given by the request
        response = requests.get(url)

    except Exception as error:
        print("\n The following exception occurred when downloading the data:\n", error)

    else:

        return response


def extractData():
    """
    Function used to get the html page where the data is stored and convert
    the wanted info into a Pandas dataframe
    """

    # We obtain the html with the data
    responseHtml = obtainData()

    # We parse the html to an BeautifulSoup object
    soup = BeautifulSoup(responseHtml.content, "html5lib")

    # We select the table in the html
    soupTable = soup.find('table')

    # We transform the html table into a Pandas dataframe
    dataframe = pd.read_html(str(soupTable))
    dataframe = dataframe[0]

    # We remove the unwanted columns from the dataframe
    dataframe = dataframe.iloc[:, :9]
    dataframe = dataframe.drop(columns=['Local'])

    # We rename the columns for better understanding of the dataframe
    dataframe.rename(columns=lambda name: name.replace(
        'Coluna', 'Dezena'), inplace=True)

    # We remove the empty rows and reset the index
    dataframe = dataframe.dropna()
    dataframe = dataframe.reset_index(drop=True)

    # We properly assign the value type of each column
    conditionMask = dataframe.columns != 'Data do Sorteio'
    dataframe.loc[:, conditionMask] = dataframe.loc[:,
                                                    conditionMask].astype("int64")

    return dataframe
