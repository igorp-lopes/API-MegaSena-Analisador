import pandas as pd


def findNewest(dataframe):

    # We obtain the column names of the selected numbers
    columnsList = dataframe.columns.tolist()
    columnsList = columnsList[2:]
    finalGroupedDataframe = pd.DataFrame({})

    for column in columnsList:
        # We group the selected numbers in each column by their earliest date
        groupedDataframe = dataframe.groupby(column)['Concurso'].max()
        groupedDataframe = groupedDataframe.reset_index()
        groupedDataframe = groupedDataframe.rename(columns={column: 'Dezena'})

        # We aṕpend each dataframe into one to gather the ocurrences in all the 6 positions
        finalGroupedDataframe = finalGroupedDataframe.append(
            groupedDataframe, ignore_index=True)

    # We group the selected numbers once again by the earliest date to obtain the earliest date between all the 6 positions
    finalGroupedDataframe = finalGroupedDataframe.groupby('Dezena')[
        'Concurso'].max()

    return finalGroupedDataframe
