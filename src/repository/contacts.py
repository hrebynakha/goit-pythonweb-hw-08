"""Contacts repo"""

from fastapi_sa_orm_filter.main import FilterCore
from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.contacts import Contact
from src.schemas.contacts import ContactModel

from src.filters.contacts import contact_filter


class ContactRepository:
    """Contact repo class"""

    def __init__(self, session: AsyncSession):
        self.db = session

    async def get_contacts(self, filter_: str, skip: int, limit: int) -> List[Contact]:
        """Get contcats in database and return by limit"""
        filter_inst = FilterCore(Contact, contact_filter)
        query = filter_inst.get_query(filter_).offset(skip).limit(limit)
        contacts = await self.db.execute(query)
        return contacts.scalars().all()

    async def get_contact_by_id(self, contact_id: int) -> Contact | None:
        """Get contact in databse by ID"""
        command = select(Contact).filter_by(id=contact_id)
        contact = await self.db.execute(command)
        return contact.scalar_one_or_none()

    async def get_contact_by_email(
        self, contact_email: str, contact_id: int = None
    ) -> Contact | None:
        """Get contact in databse by email"""
        if contact_id:
            command = select(Contact).filter(
                Contact.email == contact_email, Contact.id != contact_id
            )
        else:
            command = select(Contact).filter_by(email=contact_email)
        contact = await self.db.execute(command)
        return contact.scalar_one_or_none()

    async def create_contact(self, body: ContactModel) -> Contact:
        """Create contact function"""
        contact = Contact(**body.model_dump(exclude_unset=True))
        self.db.add(contact)
        await self.db.commit()
        await self.db.refresh(contact)
        return contact

    async def update_contact(
        self, contact_id: int, body: ContactModel
    ) -> Contact | None:
        """Update contact in database"""
        contact = await self.get_contact_by_id(contact_id)
        if contact:
            if contact.email != body.email:
                # Check if the new email already exists
                existing_contact = await self.get_contact_by_email(body.email)
                if existing_contact:
                    raise ValueError(
                        f"Contact with this email {body.email} alredy exists"
                    )
            for field, value in body.model_dump(exclude_unset=True).items():
                current_value = getattr(contact, field)
                if current_value != value:
                    setattr(contact, field, value)
            await self.db.commit()
            await self.db.refresh(contact)
        return contact

    async def remove_contact(self, contact_id: int) -> Contact | None:
        """Remove contact in DB"""
        contact = await self.get_contact_by_id(contact_id)
        if contact:
            await self.db.delete(contact)
            await self.db.commit()
        return contact

    async def search_contacts(self, limit: int = 100, **query_params) -> List[Contact]:
        """Search contcats in database and return by limit 100"""
        print(query_params)
        command = select(Contact).filter(**query_params).limit(limit)
        contacts = await self.db.execute(command)
        return contacts.scalars().all()
