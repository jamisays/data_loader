CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS Jobs (
    id SERIAL PRIMARY KEY,
    job_title TEXT,
    job_category TEXT,
    job_description TEXT,
    client_info TEXT,clean_text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

def create_job_description_table():
    """Create table if it doesn't exist"""
    from db.local.connection import get_db_connection
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(CREATE_TABLE_SQL)
        conn.commit()