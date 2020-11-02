from bs4 import BeautifulSoup
from helpers import downloadData
import pandas as pd


def extractData():
    """
    Function used to get the html page where the date is stored and convert
    the wanted info into a Pandas dataframe
    """

    # We obtain the html with the data
    responseHtml = downloadData.obtainData()

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
