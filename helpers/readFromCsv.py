import pandas as pd


def readFromCsv(filePath):
    """
    Function used to read the results from a .csv file
    and fix the columns values
    """

    dataframe = pd.read_csv(filePath, delimiter=",")

    return dataframe
