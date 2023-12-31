import requests
import os
from parsers_hh_superjob.hh_superjob_api.abc_method import VacanciApi
from parsers_hh_superjob.objects.vacancy import Vacancy


class SuperJob(VacanciApi):
    sj_key = os.getenv("Api_sj_key")

    def __init__(self):
        self._api_sj = 'https://api.superjob.ru/2.0/vacancies/'

    def get_request(self, query_text):

        response = requests.get(f"{self._api_sj}?keyword={query_text}", headers={'X-Api-App-Id': self.sj_key})
        if response.status_code == 200:
            data = response.json()
            result = []

            for sj_vacancy in data["objects"]:
                payment_from = sj_vacancy.get('payment_from', 0)
                payment_to = sj_vacancy.get('payment_to', 0)
                payment = max(payment_from, payment_to)
                vacancy = Vacancy(sj_vacancy['profession'], sj_vacancy['link'], payment, sj_vacancy['candidat'])
                result.append(vacancy)
            return result

        else:
            return []
