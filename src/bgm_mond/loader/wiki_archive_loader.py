from typing import Iterator
import zipfile
from .model import Subject, Favorite, Person, Character, Episode, Tag, ScoreDetails


class ArchiveLoader:
    # a loader to consume zipped jsonlines files, released at https://github.com/bangumi/Archive
    def __init__(self, archive_path: str):
        self.archive_path = archive_path
        self.archive = None

    def subjects(self) -> Iterator[Subject]:
        raise NotImplementedError

    def persons(self) -> Iterator[Person]:
        raise NotImplementedError
