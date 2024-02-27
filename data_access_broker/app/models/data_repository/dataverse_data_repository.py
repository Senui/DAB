from pyDataverse.api import NativeApi

class DataverseRepository:
    def __init__(self, url):
        self.name = "Dataverse data repository"
        self.url = url

    def get_download_link(self, doi):
        # Similar to MetadataRepository, this would interact with a real service.
        # The return value is hard-coded for demonstration purposes.
        if doi == "10.1000/exampledoi":
            return "http://example.com/dataset.csv"
        return "Download link not found"
