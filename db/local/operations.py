from db.base_operations import BaseDatabaseOperations


class LocalDatabaseOperations(BaseDatabaseOperations):
    def store_job_descriptions(self, data: list[dict]) -> None:
        """Store job descriptions in database with duplicate prevention"""
        from db.local.connection import get_db_connection
        
        insert_sql = """
        INSERT INTO jobs 
        (filename, job_title, job_category, job_description, client_info)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (filename) DO NOTHING
        """
        
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                for item in data:
                    try:
                        cursor.execute(insert_sql, (
                            item['filename'],  # Add filename to insert
                            item.get('job_title'),
                            item.get('job_category'),
                            item.get('job_description'),
                            item.get('client_info')
                        ))
                    except Exception as e:
                        print(f"Skipped duplicate: {item['filename']}")
                        conn.rollback()
            conn.commit()