import datetime


class Task:
    """class for create task"""
    def __init__(self, description: str, date_start: datetime, date_done: datetime, status: bool = False) -> None:
        self.__description = description
        self.__status = status
        self.__date_start = date_start
        self.__date_done = date_done

    def get_description(self) -> str:
        return self.__description

    def get_date_start(self) -> object:
        return self.__date_start

    def get_date_done(self) -> object:
        return self.__date_done

    def get_status(self) -> bool:
        return self.__status

    def set_status(self, status: bool) -> None:
        """
        Change status. if status = None: it changes to the opposite
        :param status:
        :return:
        """
        if status is None:
            self.__status = not self.__status

        else:
            self.__status = status

    def set_date_done(self, new_datetime: datetime) -> None:
        self.__date_done = new_datetime
