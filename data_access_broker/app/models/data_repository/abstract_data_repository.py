from abc import ABC, abstractmethod

class AbstractDataRepository(ABC):
    def __init__(self, name, url):
        self.name = name
        self.url = url

    @abstractmethod
    def get_download_link(self, doi) -> str:
        pass
