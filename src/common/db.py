"""
Database Connection Module

Purpose:
    Manage PostgreSQL connections
"""

from typing import Optional

import psycopg2
from psycopg2.extensions import connection

from src.common.app_config import database_config


def get_connection() -> connection:
    """
    Create PostgreSQL connection.

    Returns:
        connection: Active PostgreSQL connection

    Raises:
        psycopg2.Error
    """

    try:
        conn = psycopg2.connect(
            host=database_config.host,
            port=database_config.port,
            dbname=database_config.database,
            user=database_config.user,
            password=database_config.password,
        )

        return conn

    except psycopg2.Error as exc:
        raise RuntimeError(
            f"Database connection failed: {exc}"
        ) from exc