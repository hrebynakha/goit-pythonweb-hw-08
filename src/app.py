"""Main app entrypoint"""

from fastapi import FastAPI, Request, status
from src.api import utils, contacts

from src.execptions.core import AppHttpError, AppValueError, AppKeyError
from src.execptions.contacts import EmailValueError, ContactNotFound

app = FastAPI()

app.include_router(utils.router, prefix="/api")
app.include_router(contacts.router, prefix="/api")


@app.exception_handler(AppValueError)
async def value_exception_handler(
    request: Request, error: AppValueError  # pylint: disable=unused-argument
):
    """Value error"""
    if isinstance(error, EmailValueError):
        raise AppHttpError(detail=str(error))
    raise AppHttpError(detail="Ooops, some value error happend!")


@app.exception_handler(AppKeyError)
async def key_exception_handler(
    request: Request, error: AppValueError  # pylint: disable=unused-argument
):
    """Key error"""
    if isinstance(error, ContactNotFound):
        raise AppHttpError(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    raise AppHttpError(detail="Ooops, some value error happend!")
