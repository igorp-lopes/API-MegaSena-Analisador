from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from fastapi_utils.tasks import repeat_every
import os

from app.routers import routeResults
from app.routers import routeOccurrences
from app.routers import routeDates
from app.helpers import getData
from app.helpers import auxiliary

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("ALLOWED_ORIGINS")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routine to update the results database daily


@app.on_event('startup')
@repeat_every(seconds=(60 * 60) * 24)
def update_database():
    """
    Function that requests the results from the official database
    and saves them for use in the API
    """

    # We obtain the data from the official database
    df = getData.extractData()

    # We save the dataframe for later use in the API
    auxiliary.saveToCsv(df, 'app/resources')


app.include_router(routeResults.router)
app.include_router(routeOccurrences.router)
app.include_router(routeDates.router)
