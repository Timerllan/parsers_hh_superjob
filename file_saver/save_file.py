from parsers_hh_superjob.file_saver.abcstact_method_json import SaveFileAbstract
import json
import csv


class SaverFile(SaveFileAbstract):
    def __init__(self, data):
        self.data = data

    def _data_to_dict(self):
        list_result = []
        for vacancy in self.data:
            list_result.append({'name': vacancy.name,
                                'salary': vacancy.salary,
                                'url': vacancy.url,
                                'description': vacancy.description})
        return list_result

    def save_file_json(self, file_json):
        with open(file_json, 'w', encoding='utf-8') as file:
            json.dump(self._data_to_dict(), file, ensure_ascii=False, indent=2)

