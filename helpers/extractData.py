from bs4 import BeautifulSoup
from helpers import downloadData
import pandas as pd


def extractDataTable():
    # Obtemos a página html com os dados
    responseHtml = downloadData.obtainData()

    soup = BeautifulSoup(responseHtml.content, 'html.parser')

    tables = soup.find_all('tbody')
    tables = tables[0]
    table_rows = tables.find_all('tr')

    for row in table_rows:
        try:
            table_data = row.find_all('td')
        except:
            print("erro")

    print("Fim")

    return
