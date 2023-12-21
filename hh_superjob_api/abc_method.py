from abc import ABC, abstractmethod
from parsers_hh_superjob.objects.vacancy import Vacancy


class VacanciApi(ABC):

    @abstractmethod
    def get_request(self, query_text) -> list[Vacancy]:
        pass
