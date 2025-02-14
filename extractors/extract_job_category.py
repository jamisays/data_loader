import os


def extract_job_category(filename):
    # Remove file extension and split on last hyphen
    basename = os.path.splitext(filename)[0]
    return basename.rsplit('-', 1)[1]  # Split at last hyphen, keep left side