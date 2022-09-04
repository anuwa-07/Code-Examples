
import os

# Define CONST Variables

DATABSE_HOST = os.environ.get("DATABSE_HOST", "127.0.0.1")
DATABASE_PORT = int(os.environ.get("DATABASE_PORT", 3366))
DATABASE_USERNAME = os.environ.get("DATABASE_USERNAME", "root")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD", "12345")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "my_database")
DATABASE_POOL_SIZE = os.environ.get("DATABASE_POOL_SIZE", 2)


