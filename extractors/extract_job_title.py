import os


def extract_job_title(filename):
    # Remove file extension and split on last hyphen
    basename = os.path.splitext(filename)[0]
    return basename.rsplit('-', 1)[0]  # Split at last hyphen, keep left side