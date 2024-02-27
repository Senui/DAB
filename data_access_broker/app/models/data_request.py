from .persistent_identifier import PersistentIdentifier
from .subselection import Subselection

class DataRequest:
    def __init__(self, requester_id: str, identifiers: list[PersistentIdentifier], subselections: list[Subselection]):
        self.requester_id = requester_id
        self.identifiers = identifiers
        self.subselections = subselections
