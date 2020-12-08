from fastapi import APIRouter
from typing import Optional

router = APIRouter()


@router.get('/results')
async def getResults(startDate: Optional[str] = None):
    '''
    Route to get the unprocessed results of all the contests or in a
    subset of contests starting from a given date up to the latest contest
    '''

    # If an starting date is given, select the subset of the dataframe
    if startDate:
        tempDf = selectDateInterval(baseDf, startDate)
    else:
        tempDf = baseDf

    json = saveToJson(tempDf)

    return json
