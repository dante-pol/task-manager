from model.core import Task
import datetime


class TaskManager:
    """class for storing and working with tasks"""
    def __init__(self) -> None:
        self.__task_container = []  # container to contain task objects
        self.__count = 0    # count task objects in container

    def get_count(self) -> int:
        """
        Return count tasks in container
        :return: count tasks(int)
        """
        return self.__count

    def get_task_object(self, id: int) -> Task.Task or bool:
        """
        Return Task object for id
        :param id: is id of task
        :return: task object
        """
        if id <= 0 or id > self.__count:
            return False

        return self.__task_container[id - 1]

    def get_task_for_id(self, id) -> str or bool:
        """
        Return Task as a string
        :param id: is id of task
        :return: str
        """
        if type(self.get_task_object(id)) == bool:
            return False

        task = self.get_task_object(id)
        task_str = f'{task.get_description()} {task.get_date_start()} {task.get_date_done()} {task.get_status()}'
        return task_str

    def set_status_task(self, id: int, status: bool = None) -> bool:
        """
        Change status task and return True if operation was successful else return False
        :param status: new status of task
        :param id: is id of task
        :return: True - successful, False - error
        """
        if id <= 0 or id > self.__count:
            return False

        self.__task_container[id - 1].set_status(status)
        return True

    def set_date_done(self, id: int, date: str) -> bool:
        """
        Change date of done of task and return True if operation was successful else return False
        :param id: is id of task
        :param date: is date of format 'YY-MM-DD HH:MM'
        :return: True - successful, False - error
        """
        if id <= 0 or id > self.__count:
            return False

        date_obj = (datetime.datetime.strptime(date, '%Y-%m-%d %H:%M').isoformat(sep=' ', timespec='minutes'))
        self.__task_container[id - 1].set_date_done(date_obj)
        return True

    def create_task(self, description: str, date_start: str, date_done: str, status: bool = False) -> bool:
        """
        Create task and append it in container
        :param description: is description of task
        :param status: is current state of task
        :param date_start: is date of start of task
        :param date_done: is deadline
        :return: True - successful, False - error
        """
        try:
            date_start_obj = (datetime.datetime.strptime(date_start, '%Y-%m-%d %H:%M').
                              isoformat(sep=' ', timespec='minutes'))
            date_done_obj = (datetime.datetime.strptime(date_done, '%Y-%m-%d %H:%M').
                             isoformat(sep=' ', timespec='minutes'))

            self.__task_container.append(Task.Task(description, date_start_obj, date_done_obj, status))
            self.__count += 1
            return True

        except ValueError:
            return False

    def delete_task(self, id: int) -> bool:
        """
        Remove task from container of tasks
        :param id: is id of task
        :return: True - successful, False - error
        """
        if id < 0 or id > self.__count:
            return False

        self.__task_container.pop(id - 1)
        self.__count -= 1
        return True

    def tasks_to_save(self) -> list:
        """
        Preparing task objects to write to json file
        :return:
        """
        tasks = []
        for item in self.__task_container:
            task = {'description': item.get_description(),
                    'date_start': item.get_date_start().__str__(),
                    'date_done': item.get_date_done().__str__(),
                    'status': item.get_status()}

            tasks.append(task)

        return tasks
