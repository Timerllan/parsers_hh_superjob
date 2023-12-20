from abc import ABC, abstractmethod


class VacanciApi(ABC):

    @abstractmethod
    def get_request(self, query_text):
        pass
