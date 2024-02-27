from abc import ABC, abstractmethod

class AbstractMetadataRepository(ABC):
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def metadata_template(self):
        """Define the structure of the metadata dict to be returned by get_metadata."""
        return {
            "doi": None,
            "license": None
        }

    @abstractmethod
    def get_metadata(self, doi) -> dict:
        pass
