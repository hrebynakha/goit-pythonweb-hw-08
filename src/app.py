"""Main app entrypoint"""
from fastapi import FastAPI
from src.api import utils


app = FastAPI()


app.include_router(utils.router, prefix="/api")
