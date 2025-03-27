"""App basic configuration for models"""

from sqlalchemy.orm import DeclarativeBase
from datetime import date, datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy import Integer, String, Date, func
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.sql.sqltypes import DateTime


class Base(DeclarativeBase):
    """Base app class"""


# class Contact(Base):
#     """Contact model"""

#     __tablename__ = "contacts"
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     first_name: Mapped[str] = mapped_column(String(50), nullable=False)
#     first_name: Mapped[str] = mapped_column(String(50), nullable=False)
#     email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
#     phone: Mapped[str] = mapped_column(String(20), nullable=True)
#     birthday: Mapped[date] = mapped_column(Date, nullable=True)
#     description: Mapped[str] = mapped_column(String(255), nullable=True)
#     created_at: Mapped[datetime] = mapped_column(
#         "created_at", DateTime, default=func.now()  # pylint: disable=not-callable
#     )
#     updated_at: Mapped[datetime] = mapped_column(
#         "updated_at",
#         DateTime,
#         default=func.now(),  # pylint: disable=not-callable
#         onupdate=func.now(),  # pylint: disable=not-callable
#     )
