from typing import List

from cleaners.clean_text import clean_text
from loaders.load_raw_pdfs import load_raw_pdfs
from extractors import extract_features


def process_pdfs(folder_path: str) -> List[dict]:
    """Coordinates pipeline steps"""
    processed_data = []
    for raw_doc in load_raw_pdfs(folder_path):
        clean = clean_text(raw_doc['raw_text'])
        features = extract_features(clean, raw_doc['filename'], raw_doc['raw_text'])
        processed_data.append(features)
    return processed_data