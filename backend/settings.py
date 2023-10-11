from envparse import Env
import os

env = Env()

DATABASE_URL = env.str(
    "DATABASE_URL",
    default=f"postgresql+asyncpg://{os.environ.get('POSTGRES_USER')}:{os.environ.get('POSTGRES_PASSWORD')}@database:5432/{os.environ.get('POSTGRES_DB')}",
)