from fastapi import APIRouter
from typing import Optional

from app.helpers import dataframeAnalysis
from app.helpers import auxiliary

router = APIRouter()


@router.get('/results')
async def getResults(startDate: Optional[str] = None):
    '''
    Route to get the unprocessed results of all the contests or in a
    subset of contests starting from a given date up to the latest contest
    '''
    baseDf = auxiliary.readFromCsv('app/resources/DadosMegasena.csv')

    # If an starting date is given, select the subset of the dataframe
    if startDate:
        tempDf = dataframeAnalysis.selectDateInterval(baseDf, startDate)
    else:
        tempDf = baseDf

    json = auxiliary.saveToJson(tempDf)

    return json


@router.get('/results/{contest_number}')
async def getResults(contest_number: int):
    '''
    Route to get the unprocessed results of all the contests or in a
    subset of contests starting from a given date up to the latest contest
    '''
    baseDf = auxiliary.readFromCsv('app/resources/DadosMegasena.csv')

    # We select the given contest information
    selectionMask = baseDf['Concurso'] == contest_number
    baseDf = baseDf[selectionMask]

    json = auxiliary.saveToJson(baseDf)

    return json[0]
