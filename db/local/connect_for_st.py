from psycopg import OperationalError
from sqlalchemy import create_engine
from langchain.sql_database import SQLDatabase
# from langchain_community.utilities import SQLDatabase

def get_db_connection_2():
    """Create and return a database connection"""
    try:
        conn_str = f"postgresql+psycopg://{"postgres"}:{"jami"}@{"localhost"}:{5432}/{"job_description"}"

        # creator =  psycopg.connect(
        #     dbname="job_description",
        #     user="postgres",
        #     password="jami",
        #     host="localhost"
        # )

        engine = create_engine(conn_str)

        return SQLDatabase(engine)
    except OperationalError as e:
        print(f"Database connection error: {e}")
        raise
