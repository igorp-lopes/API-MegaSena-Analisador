import pandas as pd


def findRecurrence(dataframe):
    """
    Function used to find how many times each number has been selected as
    a winning number in a given dataframe with the results
    """

    # We select only the drawn numbers from the dataframe
    dfNumbers = dataframe.iloc[:, 2:]

    columns = list(dfNumbers)
    groupedSeries = pd.Series([])
    for i in columns:

        if groupedSeries.empty:
            groupedSeries = dfNumbers[i]
        else:
            groupedSeries = pd.concat(
                [groupedSeries, dfNumbers[i]], ignore_index=True)

    recurrenceSeries = (groupedSeries.value_counts()).sort_index()
    numbersSeries = (recurrenceSeries.index).to_series()

    recurrenceDataframe = pd.DataFrame([])
    recurrenceDataframe["Numeros"] = numbersSeries
    recurrenceDataframe["Ocorrencias"] = recurrenceSeries

    return recurrenceDataframe
