from dataclasses import dataclass
from typing import Optional


class Jobs:
    def __init__(self, 
                 job_title: Optional[str] = None,  # Optional, defaults to None
                 job_category: Optional[str] = None, # Optional, defaults to None
                 job_description: Optional[str] = None, # Optional, defaults to None
                 client_info: Optional[str] = None): # Optional, defaults to None

        self.job_title = job_title
        self.job_category = job_category
        self.job_description = job_description
        self.client_info = client_info