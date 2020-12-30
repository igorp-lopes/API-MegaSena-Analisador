import pandas as pd


def saveToJson(dataframe):
    """
    Function that converts a dataframe into a
    JSON file
    """

    json = dataframe.to_dict(orient="records")

    return json


def saveToCsv(dataframe, path):
    """
    Function that saves the given dataframe into a .csv file in the
    given path
    """

    path = path + '/DadosMegasena.csv'
    dataframe.to_csv(path, index=False)

    return


def readFromCsv(filePath):
    """
    Function used to read the results from a .csv file
    and fix the columns values
    """

    dataframe = pd.read_csv(filePath, delimiter=",")

    return dataframe
