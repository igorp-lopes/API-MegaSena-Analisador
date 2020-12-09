from fastapi import FastAPI
from typing import Optional
from app.routers import routeResults
from app.routers import routeRecurrence
from app.routers import routeDates


app = FastAPI()

app.include_router(routeResults.router)
app.include_router(routeRecurrence.router)
app.include_router(routeDates.router)
