import pandas as pd
from datetime import datetime


def selectDateInterval(datesSeries, startDate):
    """
    Function used to slice a subset of the results dataframe using a given date 
    to specify where the subset ends
    """

    # We convert the starting date to the date format
    startDate = datetime.strptime(startDate, "%d/%m/%Y")
    startDate = startDate.date()

    # We convert our date column of the dataframe to datetime
    datesSeries = pd.to_datetime(datesSeries)
    datesSeries = datesSeries.dt.date

    selectionMask = (datesSeries >= startDate)

    return selectionMask
