from parsers_hh_superjob.hh_superjob_api.hh_api import HH
from parsers_hh_superjob.hh_superjob_api.sj_api import SuperJob
from parsers_hh_superjob.objects.vacancy import Vacancy


def main():
    while True:

        user_int = int(input('выберете один из сайтов HeadHunter-1 SuperJob-0'))

        if user_int >= 2:
            print('не правильный ввод\nесть версия для слабовидящих\nздесь всего два варианта 0 или 1')
            continue

        elif user_int == 0:
            get_profession = input('введите профессию\n')
            sj = SuperJob()
            return print(sj.get_request(get_profession))

        elif user_int == 1:
            get_profession = input('введите профессию\n')
            hh = HH()
            return print(hh.get_request(get_profession))


if __name__ == '__main__':
    a = main()
