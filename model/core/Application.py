from model.core import TaskManager
from model.tools import saveloader


class Application:
    def __init__(self) -> None:
        self.__save_loader = saveloader.SaveLoader()
        self.taskmanager = TaskManager.TaskManager()

    def run(self) -> None:
        """
        Load tasks from json file
        :return:
        """
        tasks = self.__save_loader.preparing_json()
        for task in tasks:
            description = task['description']
            status = task['status']
            date_start = task['date_start']
            date_done = task['date_done']
            self.taskmanager.create_task(description, date_start, date_done, status)

    def stop(self) -> None:
        """
        Save all tasks to json file
        :return:
        """
        self.__save_loader.save(self.taskmanager.tasks_to_save())
