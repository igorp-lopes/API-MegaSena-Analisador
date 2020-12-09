from fastapi import APIRouter
from typing import Optional

from app.helpers import dataframeAnalysis
from app.helpers import auxiliary

router = APIRouter()


@router.get("/recurrence")
async def getRecurrence(startDate: Optional[str] = None):
    '''
    Route to get the total of occurrences of each number in all the contests or
    in a subset of contests starting from a given date up to the latest contest
    '''

    baseDf = auxiliary.readFromCsv('app/resources/DadosMegasena.csv')

    # If an starting date is given, select the subset of the dataframe
    if startDate:
        tempDf = dataframeAnalysis.selectDateInterval(baseDf, startDate)
    else:
        tempDf = baseDf

    recurrenceDf = dataframeAnalysis.findRecurrence(tempDf)
    json = auxiliary.saveToJson(recurrenceDf)

    return json
