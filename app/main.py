from fastapi import FastAPI
from typing import Optional
from app.routers import results


app = FastAPI()

app.include_router(results.router)

# @app.get("/results")
# async def getResults(startDate: Optional[str] = None):
#     '''
#     Route to get the unprocessed results of all the contests or in a
#     subset of contests starting from a given date up to the latest contest
#     '''

#     # If an starting date is given, select the subset of the dataframe
#     if startDate:
#         tempDf = selectDateInterval(baseDf, startDate)
#     else:
#         tempDf = baseDf

#     json = saveToJson(tempDf)

#     return json


# @app.get("/recurrence")
# async def getRecurrence(startDate: Optional[str] = None):
#     '''
#     Route to get the total of occurrences of each number in all the contests or
#     in a subset of contests starting from a given date up to the latest contest
#     '''
#     # If an starting date is given, select the subset of the dataframe
#     if startDate:
#         tempDf = selectDateInterval(baseDf, startDate)
#     else:
#         tempDf = baseDf

#     recurrenceDf = findRecurrence(tempDf)
#     json = saveToJson(recurrenceDf)

#     return json


# @app.get("/earliestDate")
# async def getNewestDate(startDate: Optional[str] = None):
#     '''
#     Route to get the earliest date in which each number has been selected in
#     all the contests or in a subset of contests starting from a given date up to the
#     latest contest
#     '''

#    # If an starting date is given, select the subset of the dataframe
#     if startDate:
#         tempDf = selectDateInterval(baseDf, startDate)
#     else:
#         tempDf = baseDf

#     earliestDateDf = findNewest(tempDf)
#     json = saveToJson(earliestDateDf)

#     return json


# @app.get("/oldestDate")
# async def getOldestDate(startDate: Optional[str] = None):
#     '''
#     Route to get the oldest date in which each number has been selected in
#     all the contests or in a subset of contests starting from a given date up to the
#     latest contest
#     '''

#    # If an starting date is given, select the subset of the dataframe
#     if startDate:
#         tempDf = selectDateInterval(baseDf, startDate)
#     else:
#         tempDf = baseDf

#     oldestDateDf = findOldest(tempDf)
#     json = saveToJson(oldestDateDf)

#     return json
