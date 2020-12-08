import pandas as pd


def saveToJson(dataframe):
    """
    Function that converts a dataframe into a
    JSON file
    """

    json = dataframe.to_json(orient="records")

    return json
