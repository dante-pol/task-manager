import json


class SaveLoader:
    def __read(self) -> dict:
        """
        Reading json file
        :return: dictionary of tasks
        """
        with open('model/data/tasks.json', 'r', encoding='utf8') as file:
            dictionary = json.load(file)
            return dictionary

    def preparing_json(self) -> list:
        """
        Preparing info from read json file
        :return: list of tasks(dictionaries)
        """
        tasks = self.__read()
        lst_tasks = tasks['tasks']
        return lst_tasks

    def save(self, tasks: list) -> None:
        """
        Save all changes to json file
        :param tasks: dictionary of tasks
        :return:
        """
        with open('model/data/tasks.json', 'r', encoding='utf8') as file:
            data = json.load(file)
            data['tasks'] = tasks

        with open('model/data/tasks.json', 'w', encoding='utf8') as file:
            json.dump(data, file)
