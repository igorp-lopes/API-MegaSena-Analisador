import pandas as pd


def findRecurrency(dataframe):
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

    recurrencySeries = (groupedSeries.value_counts()).sort_index()
    numbersSeries = (recurrencySeries.index).to_series()

    recurrencyDataframe = pd.DataFrame([])
    recurrencyDataframe["Numeros"] = numbersSeries
    recurrencyDataframe["Ocorrencias"] = recurrencySeries

    return recurrencyDataframe
