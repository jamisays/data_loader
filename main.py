## Data, pipeline imports
from db.operations import store_job_descriptions
from pipelines.pl import process_pdfs
from streamlit_app.run_streamlit_app import run_streamlit_app
from utils import display_job_descriptions


if __name__ == "__main__":
    # To maintain original functionality, you can add a CLI switch
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['process', 'app'], default='app')
    args = parser.parse_args()

    if args.mode == 'process':
        # Original processing code
        processed_data = process_pdfs("pdf/")
        store_job_descriptions(processed_data)
        display_job_descriptions(processed_data)
    else:
        # Run Streamlit app
        run_streamlit_app()

# # For Streamlit app
# streamlit run main.py

# # For processing pipeline
# python main.py --mode=process


