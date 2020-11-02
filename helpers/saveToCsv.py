import pandas as pd


def saveToCsv(dataframe, path):
    """
    Function that saves the given dataframe into a .csv file in the
    given path
    """

    path = path + '/DadosMegasena.csv'
    dataframe.to_csv(path, index=False)

    return
