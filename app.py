from fastapi import FastAPI

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
async def getRecurrency():

    recurrencyDf = findRecurrency(baseDf)
    json = saveToJson(recurrencyDf)

    return json
