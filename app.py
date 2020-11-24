from fastapi import FastAPI
from typing import Optional

from helpers.saveToCsv import saveToCsv
from helpers.saveToJson import saveToJson
from helpers.readFromCsv import readFromCsv
from helpers.extractData import extractData
from helpers.selectDateInterval import selectDateInterval
from helpers.findRecurrency import findRecurrency
from helpers.findDates import findNewest, findOldest

app = FastAPI()

baseDf = readFromCsv('resources/DadosMegasena.csv')


@app.get("/recurrency")
async def getRecurrency(startDate: Optional[str] = None):
    '''
    Route to get the total of ocurrences of each number in all the contests or
    in a subset of contests starting from a given date up to the latest contest
    '''
    # If an starting date is given, select the subset of the dataframe
    if startDate:
        tempDf = selectDateInterval(baseDf, startDate)
    else:
        tempDf = baseDf

    recurrencyDf = findRecurrency(tempDf)
    json = saveToJson(recurrencyDf)

    return json


@app.get("/earliestDate")
async def getNewestDate(startDate: Optional[str] = None):
    '''
    Route to get the earliest date in which each number has been selected in
    all the contests or in a subset of contests starting from a given date up to the
    latest contest
    '''

   # If an starting date is given, select the subset of the dataframe
    if startDate:
        tempDf = selectDateInterval(baseDf, startDate)
    else:
        tempDf = baseDf

    earliestDateDf = findNewest(tempDf)
    json = saveToJson(earliestDateDf)

    return json


@app.get("/oldestDate")
async def getOldestDate(startDate: Optional[str] = None):
    '''
    Route to get the oldest date in which each number has been selected in
    all the contests or in a subset of contests starting from a given date up to the
    latest contest
    '''

   # If an starting date is given, select the subset of the dataframe
    if startDate:
        tempDf = selectDateInterval(baseDf, startDate)
    else:
        tempDf = baseDf

    oldestDateDf = findOldest(tempDf)
    json = saveToJson(oldestDateDf)

    return json
