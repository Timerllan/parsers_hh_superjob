from abc_method import VacanciApi
import requests


class SuperJob(VacanciApi):
    get_params = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self, api_sj: str):
        self._api_sj = api_sj

    def get_request(self):
        return requests.get(self._api_sj)


