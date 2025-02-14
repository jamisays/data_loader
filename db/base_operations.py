from abc import ABC, abstractmethod

class BaseDatabaseOperations(ABC):
    @abstractmethod
    def store_job_descriptions(self, data: list[dict]) -> None:
        """Abstract method for storing job descriptions"""
        pass