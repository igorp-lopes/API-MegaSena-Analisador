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
    # If an starting date is given, select the subset of the dataframe
    if startDate:
        tempDf = selectDateInterval(baseDf, startDate)
    else:
        tempDf = baseDf

    recurrencyDf = findRecurrency(tempDf)
    json = saveToJson(recurrencyDf)

    return json
