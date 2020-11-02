import pandas as pd
from datetime import datetime


def selectDateInterval(datesSeries, startDate):

    # We convert the starting date to the date format
    startDate = datetime.strptime(startDate, "%d/%m/%Y")
    startDate = startDate.date()

    # We convert our date column of the dataframe to datetime
    datesSeries = pd.to_datetime(datesSeries)
    datesSeries = datesSeries.dt.date

    selectionMask = (datesSeries >= startDate)

    return selectionMask
