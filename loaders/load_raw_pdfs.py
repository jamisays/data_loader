import os
from typing import List

from model import Jobs

from .load_raw_text_from_pdf import load_raw_text_from_pdf


def load_raw_pdfs(folder_path: str) -> List[dict]:
    """Pure file loading without processing"""
    return [
        {
            "filename": filename,
            "raw_text": load_raw_text_from_pdf(os.path.join(folder_path, filename), filename)
        }
        for filename in os.listdir(folder_path)
        if filename.endswith('.pdf')
    ]