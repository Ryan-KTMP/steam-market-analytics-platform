"""
Application Configuration Module

Purpose:
    - Load environment variables
    - Validate required settings
    - Provide strongly typed configuration objects

Author:
    Steam Market Analytics Platform
"""

from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv


# ============================================================
# Load .env
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[2]
ENV_PATH = BASE_DIR / ".env"

load_dotenv(
    dotenv_path=ENV_PATH,
    override=False
)


# ============================================================
# Dataclasses
# ============================================================

@dataclass(frozen=True)
class DatabaseConfig:
    """
    Database connection configuration.
    """

    host: str
    port: int
    database: str
    user: str
    password: str


# ============================================================
# Helper Functions
# ============================================================

def get_required_env(variable_name: str) -> str:
    """
    Retrieve required environment variable.

    Raises:
        ValueError: If variable is missing.
    """

    value = os.getenv(variable_name)

    if not value:
        raise ValueError(
            f"Missing required environment variable: {variable_name}"
        )

    return value


# ============================================================
# Build Configuration
# ============================================================

database_config = DatabaseConfig(
    host=get_required_env("POSTGRES_HOST"),
    port=int(get_required_env("POSTGRES_PORT")),
    database=get_required_env("POSTGRES_DB"),
    user=get_required_env("POSTGRES_USER"),
    password=get_required_env("POSTGRES_PASSWORD"),
)