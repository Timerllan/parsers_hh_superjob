from abc_method import VacanciApi
import requests


class HH(VacanciApi):

    api_key = 'https://api.hh.ru/vacancies'
    @classmethod
    def get_request(cls):
        return requests.get(cls.api_key)


