import pandas as pd
from datetime import datetime


def selectDateInterval(dataframe, startDate):
    """
    Function used to slice a subset of the results dataframe using a given date 
    to specify where the subset ends
    """

    # We convert the starting date to the date format
    startDate = datetime.strptime(startDate, "%d/%m/%Y")
    startDate = startDate.date()

    # From the dataframe we extract the columns relative to the dates
    datesSeries = dataframe["Data do Sorteio"]

    # We convert our date column of the dataframe to datetime
    datesSeries = pd.to_datetime(datesSeries, format="%d/%m/%Y")
    datesSeries = datesSeries.dt.date

    # We create a mask to select only the rows whose date are older than the start date
    selectionMask = (datesSeries >= startDate)

    return dataframe[selectionMask]
