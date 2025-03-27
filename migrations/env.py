"""Env migartions file"""

import asyncio
from logging.config import fileConfig

from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config
from sqlalchemy import pool
from alembic import context

from src.conf.config import config as conf
from src.database.basic import Base

config = context.config  # pylint: disable=no-member

if config.config_file_name is not None:
    fileConfig(config.config_file_name)


target_metadata = Base.metadata
config.set_main_option("sqlalchemy.url", conf.get_db_url())
print(target_metadata)


def run_migrations(connection: Connection):
    """Run migration function"""
    context.configure(  # pylint: disable=no-member
        connection=connection, target_metadata=target_metadata
    )
    with context.begin_transaction():  # pylint: disable=no-member
        context.run_migrations()  # pylint: disable=no-member


async def run_async_migrations():
    """Run migration async"""
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    asyncio.run(run_async_migrations())


if not context.is_offline_mode():  # pylint: disable=no-member
    run_migrations_online()
