from parsers_hh_superjob.hh_superjob_api.abc_method import VacanciApi
import requests
from parsers_hh_superjob.objects.vacancy import Vacancy


class HH(VacanciApi):

    def __init__(self):
        self.url = 'https://api.hh.ru/'

    def get_request(self, query_text):
        data = requests.get(f'{self.url}vacancies/?text={query_text}').json()

        result = []

        for hh_vacancy in data['items']:
            salary_hh = hh_vacancy.get('salary')

            if salary_hh:
                salary_from = salary_hh.get('to', 0) if salary_hh.get('to') else 0
                salary_to = salary_hh.get('to') if salary_hh.get('to') else 0
                salary = salary_from if salary_from else salary_to


            else:
                salary = 'не указана'

            vacancy = Vacancy(hh_vacancy['name'], hh_vacancy['apply_alternate_url'], salary,
                              hh_vacancy['snippet']['requirement'])
            result.append(vacancy)
        return result
