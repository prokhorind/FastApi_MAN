import os


class Config:
    # Path to the file-based "database"
    TEXT_DB_PATH = os.getenv("TEXT_DB_PATH", "data.txt")

    # Example database connection string (for future migration)
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data.db")
