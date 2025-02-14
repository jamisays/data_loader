from .extract_job_title import extract_job_title
from .extract_job_description import extract_job_description
from .extract_job_category import extract_job_category
from .divide_client_info import extract_client_info


def extract_features(clean_text, filename, raw_text) -> dict:
    """Pure feature extraction"""
    client_info_portion, clean_text = extract_client_info(clean_text)
    return {
        "filename": filename,
        "job_title": extract_job_title(filename),
        "job_category": extract_job_category(filename),
        "job_description": extract_job_description(clean_text),
        "client_info": client_info_portion,
    }