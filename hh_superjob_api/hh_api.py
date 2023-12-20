from abc_method import VacanciApi
import requests


class HH(VacanciApi):

    def __init__(self, ):
        self.url = 'https://api.hh.ru/'

    def get_request(self, query_text):
        return requests.get(f'{self.url}vacancies/?text={query_text}')



