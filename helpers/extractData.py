from bs4 import BeautifulSoup
from helpers import downloadData
import pandas as pd


def extractData():

    def saveToDataframe(datalist, row):
        row = row.find_all('td')

        # List where we'll save the data to append to the dataframe
        rowData = []

        for index, data in enumerate(row):
            # If we are past the index of the last data we want to collect
            if index >= 8:
                break

            rowData.append(data.text)

        # We append the data from the row to the list of all the rows data
        datalist.append(rowData)
        return datalist

    # We obtain the html with the data
    responseHtml = downloadData.obtainData()

    # We parse the html to an BeautifulSoup object
    soup = BeautifulSoup(responseHtml.content, 'html.parser')

    # We select the table data from the html
    tables = soup.find_all('tbody')
    tables = tables[0]
    table_rows = tables.find_all('tr')

    # For each row of data we extract the wanted information and save it on a list of lists
    listOfData = []
    for row in table_rows:

        listOfData = saveToDataframe(listOfData, row)

    dataframeColumns = ["Concurso", "Local", "Data do Sorteio", "Coluna 1",
                        "Coluna 2", "Coluna 3", "Coluna 4", "Coluna 5", "Coluna 6"]
    print("Fim")

    dataframe = pd.DataFrame(listOfData, columns=dataframeColumns)

    return dataframe
