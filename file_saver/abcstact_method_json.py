from abc import ABC, abstractmethod


class SaveFileAbstract(ABC):
    @abstractmethod
    def save_file_json(self, file_json):
        pass

