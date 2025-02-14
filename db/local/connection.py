import psycopg
from psycopg import OperationalError

def get_db_connection():
    """Create and return a database connection"""
    try:
        return psycopg.connect(
            dbname="job_description",
            user="postgres",
            password="jami",
            host="localhost"
        )
    except OperationalError as e:
        print(f"Database connection error: {e}")
        raise
