import re

def remove_special_patterns(raw_text: str) -> str:
    """
    Removes the specific multi-line text:
    "Specialized profiles can help you better
    highlight your expertise when submitting
    proposals to jobs like these. Create a
    specialized profile."
    
    Preserves the original raw_text format, including line breaks.
    """
    # Define the multi-line text to be removed
    target_text = (
        r"Specialized profiles can help you better\n"
        r"highlight your expertise when submitting\n"
        r"proposals to jobs like these\. Create a\n"
        r"specialized profile\."
    )
    
    # Create a regex pattern for the target text
    # Use re.DOTALL to handle any potential variations in whitespace/newlines
    pattern = re.compile(target_text, flags=re.IGNORECASE | re.MULTILINE | re.DOTALL)
    
    # Remove the target text
    cleaned_text = pattern.sub('', raw_text)
    
    # Post-processing: Normalize excessive newlines caused by removal
    # Split into lines and filter out empty lines
    lines = cleaned_text.split('\n')
    cleaned_lines = [line for line in lines if line.strip()]  # Keep non-empty lines
    
    # Rejoin lines with '\n' to preserve the original format
    return '\n'.join(cleaned_lines).strip()