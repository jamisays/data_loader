## Data, pipeline imports
from db.local.operations import LocalDatabaseOperations
from db.supabase.operations import SupabaseOperations
from pipelines.pl import process_pdfs
from streamlit_app.run_streamlit_app import run_streamlit_app
from utils import display_job_descriptions


if __name__ == "__main__":
    # Set up argument
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['process', 'app'], default='app')
    args = parser.parse_args()

    if args.mode == 'process':
        # Original processing code
        processed_data = process_pdfs("pdf/")

        # Store to local PostgreSQL
        local_db = LocalDatabaseOperations()
        local_db.store_job_descriptions(processed_data)

        # Store to Supabase
        supabase_db = SupabaseOperations()
        supabase_db.store_job_descriptions(processed_data)

        display_job_descriptions(processed_data)
    else:
        # Run Streamlit app
        run_streamlit_app()


# streamlit run main.py

# python main.py --mode=process


