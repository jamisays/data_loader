import re


def remove_metadata(raw_text:str) -> str:
    """
    Removes PDF footer metadata patterns like:
    "MM/DD/YY, HH:MM PM [Job Title] [URL] X/Y"
    """
    # Pattern explanation:
    # 1. Date (MM/DD/YY or MM/DD/YYYY)
    # 2. Time (HH:MM AM/PM)
    # 3. Job title text
    # 4. URL pattern
    # 5. Page number (X/Y)
    pattern = r"""
        ^\d{1,2}/\d{1,2}/\d{2,4},     # Date
        \s+\d{1,2}:\d{2}\s+[AP]M      # Time
        .+?                           # Job title text
        https?://\S+                  # URL
        \s+\d+/\d+                    # Page number
        $                             # End of line
    """
    
    # Remove metadata using regex
    cleaned_text = re.sub(
        pattern=pattern,
        repl='',
        string=raw_text,
        flags=re.VERBOSE | re.MULTILINE | re.IGNORECASE | re.DOTALL
    )
    
    # Post-processing: Remove empty lines
    lines = cleaned_text.split('\n')  # Split into lines
    non_empty_lines = [line for line in lines if line.strip()]  # Filter out empty lines
    
    # Join the remaining lines with newlines
    return '\n'.join(non_empty_lines).strip()