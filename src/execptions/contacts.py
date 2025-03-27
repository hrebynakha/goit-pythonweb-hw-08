"""Execption module"""

from src.execptions.core import AppKeyError, AppValueError


class EmailValueError(AppValueError):
    """Email validation error"""


class EntityNotFound(AppKeyError):
    """Entity not found in database"""


class ContactNotFound(EntityNotFound):
    """Contact not found in database"""
