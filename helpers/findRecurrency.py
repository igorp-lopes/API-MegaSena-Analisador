import pandas as pd


def findRecurrency(dataframe):
    """
    Function used to find how many times each number has been selected as
    a winning number in a given dataframe with the results
    """

    # We select only the drawn numbers from the dataframe
    dfNumbers = dataframe.iloc[:, 2:]

    return dfNumbers
