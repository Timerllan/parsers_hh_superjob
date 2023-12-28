from parsers_hh_superjob.file_saver.save_file import SaverFile
from parsers_hh_superjob.hh_superjob_api.hh_api import HH
from parsers_hh_superjob.hh_superjob_api.sj_api import SuperJob


def main():
    while True:

        user_int = int(input('выберете один из сайтов HeadHunter-1 SuperJob-0\n'))

        if user_int >= 2:
            print('не правильный ввод\nесть версия для слабовидящих\nздесь всего два варианта 0 или 1')
            continue

        elif user_int == 0:
            get_profession = input('введите профессию\n')
            sj = SuperJob()
            result = sj.get_request(get_profession)
            return result

        elif user_int == 1:
            get_profession = input('введите профессию\n')
            hh = HH()
            result = hh.get_request(get_profession)
            return result


def format_saver(result):
    while True:
        saver = int(input('сохранение файла 0-json\n'))
        file_name = input('назовите файл')
        if saver >= 1:
            print('не правильный ввод есть только 1 вариант')
            continue

        elif saver == 0:
            sf = SaverFile(result)
            sf.save_file_json(file_name)
            break


if __name__ == '__main__':
    a = main()
    b = format_saver(a)
