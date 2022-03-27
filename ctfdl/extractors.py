import zipfile
import tarfile
from typing import List

class Extractor:
    def __init__(self, path: str):
        pass

    def list(self) -> List[str]:
        return []

    def extract(self, dest: str):
        return []


class ZipExtractor(Extractor):
    def __init__(self, path: str):
        self.archive = zipfile.open(path, 'r')

    def list(self) -> List[str]:
        return []

    def extract(self, dest: str) -> List[str]:
        return []


class TarExtractor(Extractor):
    def __init__(self, path: str):
        self.archive = tarfile.open(path, 'r')

    def list(self) -> List[str]:
        names = self.archive.getnames()
        for i in range(len(names)):
            if names[i].startswith('./'):
                names[i] = names[i][2:]
        return names

    def extract(self, dest: str):
        self.archive.extractall(dest)
