from unittest.mock import MagicMock
from unittest.mock import patch

# from app.services.data_access_request_handler import DataAccessRequestHandler
# from app.models.data_request import DataRequest
from app.models.metadata_repository.odissei_metadata_repository import (
    OdisseiMetadataRepository,
)

# from app.models.data_repository import DataRepository

import json, os


# Fetch the data license of a test dataset (raw metadata is stored in `raw_odissei_metadata.json`)
def test_get_metadata_odissei_metadata_portal():
    file_path = os.path.join(os.path.dirname(__file__), "raw_odissei_metadata.json")
    with open(file_path, "r") as file:
        mock_data = json.load(file)

    # Override `fetch_raw_metadata` call to bypass the actuall API call to the ODISSEI portal
    with patch(
        "app.models.metadata_repository.odissei_metadata_repository.OdisseiMetadataRepository.fetch_raw_metadata",
        return_value=mock_data,
    ):
        repository = OdisseiMetadataRepository()
        doi = "doi:10.17026/SS/M9AOZD"
        metadata = repository.get_metadata(doi)
        assert (
            metadata["license"] == "CC0 1.0"
        ), "The CC0 1.0 license should be fetched from the ODISSEI metadata repository"
        assert (
            metadata["doi"] == "doi:10.17026/SS/M9AOZD"
        ), "The doi should be fetched from the ODISSEI metadata repository"


# @pytest.fixture
# def mock_data_repository(mocker):
#     # Mocking the Data Repository to return a download link
#     mock = mocker.MagicMock(spec=DataRepository)
#     mock.get_download_link.return_value = "http://example.com/dataset.csv"
#     return mock


# @pytest.fixture
# def data_access_request_handler(mock_metadata_repository, mock_data_repository):
#     # Injecting the mocked repositories into the Data Access Request Handler
#     return DataAccessRequestHandler(
#         metadata_repository=mock_metadata_repository,
#         data_repository=mock_data_repository,
#     )


# def test_request_open_access_doi(data_access_request_handler):
#     # Simulate a researcher requesting access by DOI
#     doi = "doi:10.17026/SS/M9AOZD"
#     download_link = data_access_request_handler.request_access(doi)

#     # Verify the data repository was queried for the download link
#     assert (
#         download_link == "http://example.com/dataset.csv"
#     ), "The download link should be retrieved from the data repository for open-access data"
