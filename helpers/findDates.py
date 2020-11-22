import pandas as pd


def __groupByContestNumber(dataframe, highest):
    """
    Helper function that obtains the highest or lowest contest numbers 
    of each selected numbers
    """

    # We obtain the column names of the selected numbers
    columnsList = dataframe.columns.tolist()
    columnsList = columnsList[2:]
    finalGroupedDataframe = pd.DataFrame({})

    for column in columnsList:
        # We group the selected numbers in each column either by the highest or lowest contest number
        if highest:
            groupedDataframe = dataframe.groupby(column)['Concurso'].max()
        else:
            groupedDataframe = dataframe.groupby(column)['Concurso'].min()

        groupedDataframe = groupedDataframe.reset_index()
        groupedDataframe = groupedDataframe.rename(columns={column: 'Dezena'})

        # We aṕpend each dataframe into one to gather the ocurrences in all the 6 positions
        finalGroupedDataframe = finalGroupedDataframe.append(
            groupedDataframe, ignore_index=True)

    # We group the selected numbers once again by the earliest date to obtain the highest or lowest contest number between all the 6 positions
    if highest:
        finalGroupedDataframe = finalGroupedDataframe.groupby('Dezena')[
            'Concurso'].max()
    else:
        finalGroupedDataframe = finalGroupedDataframe.groupby('Dezena')[
            'Concurso'].min()

    return finalGroupedDataframe


def __convertContestToDate(dataframe, contestDataframe):
    """
    Helper function that converts the contest number to their
    respective dates
    """
    # From the dataframe, we get the dates relative to each obtained contest
    dateSelectionMask = dataframe['Concurso'].isin(contestDataframe)
    tempDf = dataframe[dateSelectionMask]
    tempDf = tempDf[['Concurso', 'Data do Sorteio']]

    # We transform the new dataframe with the dates into a dict
    dataframeToDict = tempDf.set_index('Concurso')
    dataframeToDict = dataframeToDict.transpose()
    dataframeToDict = dataframeToDict.to_dict(orient='list')
    dataframeToDict = {key: value[0] for key, value in dataframeToDict.items()}

    # From the dict we map the dataframe changing the contest numbers to the actual dates
    contestDataframe = contestDataframe.map(dataframeToDict)

    # We transform the series with the dates into our final dataframe with the numbers and their dates
    finalDataframe = pd.DataFrame(
        {'Dezenas': contestDataframe.index, 'Data': contestDataframe.values})

    return finalDataframe


def findNewest(dataframe):

    # We group the selected numbers by their highest contest number
    contestOrderedSeries = __groupByContestNumber(dataframe, highest=True)

    # We convert the contest number into the actual date
    datesDataframe = __convertContestToDate(dataframe, contestOrderedSeries)

    return datesDataframe
