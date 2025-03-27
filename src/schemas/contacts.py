"""Contacts validation schema"""

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, PastDate
from pydantic_extra_types.phone_numbers import PhoneNumber


class ContactModel(BaseModel):
    """Base contact model"""

    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: EmailStr = Field(max_length=255)
    phone: Optional[PhoneNumber] = Field(default=None, max_length=20)
    birthday: Optional[PastDate] = None
    description: Optional[str] | None = Field(default=None, max_length=255)


class ContactResponse(ContactModel):
    """Response model"""

    id: int
    created_at: datetime
    updated_at: datetime


# class TagResponse(TagModel):
#     id: int

#     model_config = ConfigDict(from_attributes=True)


# class NoteBase(BaseModel):
#     title: str = Field(max_length=50)
#     description: str = Field(max_length=150)


# class NoteModel(NoteBase):
#     tags: List[int]


# class NoteUpdate(NoteModel):
#     done: bool


# class NoteStatusUpdate(BaseModel):
#     done: bool


# class NoteResponse(NoteBase):
#     id: int
#     done: bool
#     created_at: datetime | None
#     updated_at: Optional[datetime] | None
#     tags: List[TagResponse] | None

#     model_config = ConfigDict(from_attributes=True)
