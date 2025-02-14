from db.supabase.connection import get_supabase_connection
from db.base_operations import BaseDatabaseOperations

class SupabaseOperations(BaseDatabaseOperations):
    def __init__(self):
        self.client = get_supabase_connection()
    
    def store_job_descriptions(self, data: list[dict]) -> None:
        """Store job descriptions in Supabase"""
        try:
            response = (
                self.client.table("jobs")
                .upsert(
                    [self._prepare_data(item) for item in data],
                    on_conflict="filename",  # Name of the unique constraint

                    ignore_duplicates=True   # Supabase-specific option
                    )
                .execute()
            )
            inserted_count = len(response.data)
            total_count = len(data)
            
            if inserted_count < total_count:
                print(f"Skipped {total_count - inserted_count} duplicates")
                
            print(f"Inserted {inserted_count} new records into Supabase")
        except Exception as e:
            if '23505' in str(e):  # PostgreSQL duplicate key error code
                print("Duplicate entries skipped")
            else:
                print(f"Supabase error: {e}")
                raise
    
    def _prepare_data(self, item: dict) -> dict:
        """Prepare data for Supabase insertion"""
        return {
            "filename": item["filename"],
            "job_title": item.get("job_title"),
            "job_category": item.get("job_category"),
            "job_description": item.get("job_description"),
            "client_info": item.get("client_info")
        }