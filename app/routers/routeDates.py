from fastapi import APIRouter
from typing import Optional

from app.helpers import dataframeAnalysis
from app.helpers import auxiliary

router = APIRouter()


@router.get("/dates/earliest")
async def getNewestDate(startDate: Optional[str] = None):
    '''
    Route to get the earliest date in which each number has been selected in
    all the contests or in a subset of contests starting from a given date up to the
    latest contest
    '''

    baseDf = auxiliary.readFromCsv('app/resources/DadosMegasena.csv')

   # If an starting date is given, select the subset of the dataframe
    if startDate:
        tempDf = dataframeAnalysis.selectDateInterval(baseDf, startDate)
    else:
        tempDf = baseDf

    earliestDateDf = dataframeAnalysis.findNewest(tempDf)
    json = auxiliary.saveToJson(earliestDateDf)

    return json


@router.get("/dates/oldest")
async def getOldestDate(startDate: Optional[str] = None):
    '''
    Route to get the oldest date in which each number has been selected in
    all the contests or in a subset of contests starting from a given date up to the
    latest contest
    '''

    baseDf = auxiliary.readFromCsv('app/resources/DadosMegasena.csv')

   # If an starting date is given, select the subset of the dataframe
    if startDate:
        tempDf = dataframeAnalysis.selectDateInterval(baseDf, startDate)
    else:
        tempDf = baseDf

    oldestDateDf = dataframeAnalysis.findOldest(tempDf)
    json = auxiliary.saveToJson(oldestDateDf)

    return json
