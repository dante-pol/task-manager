from model.core import TaskManager


class WebPresenter:
    @staticmethod
    def get_task(id: int, taskmanager: type(TaskManager.TaskManager)):
        """
        Returning task as a string
        :param id: is id of task
        :param taskmanager: object of class TaskManager
        :return: string - '<description> <date_start> <date_done> <status>'
        """
        return taskmanager.get_task_for_id(id)
