from .remove_metadata import remove_metadata
from .remove_special_patterns import remove_special_patterns


def clean_text(raw_text: str) -> str:
    """Focuses only on text normalization"""
    text = remove_metadata(raw_text)
    # client_info_portion = clean_client_info_portion(client_info_portion)
    text = remove_special_patterns(text)
    return text