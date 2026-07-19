"""Database seed data — run once after initial migration."""

import asyncio

from sqlalchemy import select

from app.core.database import async_session_factory
from app.models.user import User


async def seed_default_data() -> None:
    """Create default seed data if not already present."""
    async with async_session_factory() as session:
        # Check if any user exists
        result = await session.execute(select(User).limit(1))
        if result.scalar_one_or_none() is not None:
            print("Seed data already exists — skipping.")
            return

        # Create default admin user
        # Password must be set through the application (hashed via Argon2id)
        print("No users found. Run the application setup to create the admin user.")
        print("Seed check complete.")


if __name__ == "__main__":
    asyncio.run(seed_default_data())
