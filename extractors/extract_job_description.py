import re

def extract_job_description(raw_text: str) -> str:
    """
    Extracts the job description from raw_text.
    
    Job description starts after the word 'Worldwide' on a new line.
    Job description ends when:
    1. 'More than' or 'Less than' is found (e.g., 'More than 30', 'Less than 30'), or
    2. A dollar amount is found (e.g., $50.00, $100.00).
    
    Preserves the raw_text format, including line breaks.
    """
    # Define regex patterns for start and end conditions
    start_pattern = r"^Worldwide\s*$"  # Matches 'Worldwide' on a new line
    end_pattern = r"(More than|Less than|\$\d+\.\d{2})"  # Matches 'More than', 'Less than', or dollar amounts
    
    # Split the text into lines
    lines = raw_text.split('\n')
    
    # Initialize variables
    start_index = None
    end_index = None
    
    # Find the start index
    for i, line in enumerate(lines):
        if re.match(start_pattern, line, flags=re.IGNORECASE):
            start_index = i + 1  # Start after the 'Worldwide' line
            break
    
    # If no start index is found, return an empty string
    if start_index is None:
        return ""
    
    # Find the end index
    for i in range(start_index, len(lines)):
        if re.search(end_pattern, lines[i], flags=re.IGNORECASE):
            end_index = i
            break
    
    # If no end index is found, include all lines until the end
    if end_index is None:
        end_index = len(lines)
    
    # Extract the job description lines
    job_description_lines = lines[start_index:end_index]
    
    # Rejoin the lines with '\n' to preserve the original format
    return '\n'.join(job_description_lines).strip()