def extract_client_info(raw_text: str) -> tuple[str, str]:
    """
    Extracts text between 'Apply now' and 'Copy link' lines (inclusive),
    returns (extracted_text, cleaned_text)
    """
    lines = raw_text.split('\n')
    start_idx = None
    end_idx = None

    # Find start and end markers
    for i, line in enumerate(lines):
        if line.strip() == 'Apply now':
            start_idx = i
        if line.strip() == 'Copy link' and start_idx is not None:
            end_idx = i
            break  # Stop at first occurrence after start

    if start_idx is not None and end_idx is not None and start_idx < end_idx:
        # Extract client info
        client_info = '\n'.join(lines[start_idx:end_idx+1])
        
        # Remove these lines from original text
        cleaned_lines = lines[:start_idx] + lines[end_idx+1:]
        cleaned_text = '\n'.join(cleaned_lines)
        
        return client_info, cleaned_text
    
    # Return original text if markers not found
    return "", raw_text