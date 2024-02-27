import logging

from .abstract_metadata_repository import AbstractMetadataRepository
from pyDataverse.api import NativeApi

logger = logging.getLogger(__name__)

class OdisseiMetadataRepository(AbstractMetadataRepository):
    def __init__(self):
        self.name = "ODISSEI metadata repository"
        self.url = "https://portal.odissei.nl"

    def get_metadata(self, doi):
        raw_data = self.fetch_raw_metadata(doi)
        return self.parse_metadata(raw_data)

    def fetch_raw_metadata(self, doi):
        api = NativeApi(self.url)
        response = api.get_dataset(doi)
        response.raise_for_status()
        return response.json()

    def parse_metadata(self, raw_data):
        metadata = self.metadata_template()
        try:
            metadata['doi'] = raw_data['data']['latestVersion']['datasetPersistentId']
        except KeyError:
            logger.warning('DOI missing in metadata for raw_data: %s', raw_data)
            metadata['doi'] = None

        try:
            metadata['license'] = raw_data['data']['latestVersion']['license']['name']
        except KeyError:
            logger.warning('License information missing in metadata')
            metadata['license'] = None

        return metadata
