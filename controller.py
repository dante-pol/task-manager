from model.core import TaskManager, WebPresenter
import eel


@eel.expose
def get_one_task(id: int) -> str:
    """
    Вернет Task по ID, формат возврата <!--надо дописать--!>, тип данных str
    :param id: int - идентификатор Task
    :return: str - Task
    """
    pass


@eel.expose
def get_all_task() -> str:
    """
    Эта функция под вопросом.
    :return:
    """
    pass


@eel.expose
def create_task(descript: str, start_time: str, deadline: str, is_done: bool = False) -> bool:
    """
    Создание новой Task, принимает на вход необходимое количество входных данных, возвращает значение bool,
    указывающий на успешность выполнения команды.
    :param descript: type = str, описание самой задачи
    :param start_time: type = str, начальное время на выполнение задачи, должно иметь формат 'YY-MM-DD HH:MM"
    :param deadline: начальное время на выполнение задачи, должно иметь формат 'YY-MM-DD HH:MM"
    :param is_done: Статус задачи (В работе = False, выполнена = True). По умолчанию имеет статус False.
    :return: Вернет True, если задача успешно создана, либо False, если в процессе создания возникли какие либо ошибки,
             из-за которых задача не может быть создана.
    """
    pass



@eel.expose
def remove_task(id: int) -> bool:
    """
    Удаляет указанный пользователем Task
    :param id: int - идентификатор Task
    :return: Вернет True, если задача успешно удалена, либо False, если в процессе удаления возникли какие либо ошибки,
             из-за которых задача не может быть удалена.
    """
    pass


@eel.expose
def switch_status(id: int) -> str:
    """
    Меняет статус выполнения Task на противоположный. Вернет обновленную информацию о Task, формат возврата
    <!--надо дописать--!>, тип данных str
    :param id: int - идентификатор Task
    :return: str - Task
    """
    pass


@eel.expose
def add_time_for_deadline(id: str, time: str) -> bool:
    """
    Добавит время к атрибуте Task, который показывает конечное время выполнения. Task находим по ID. Для правильной
    работы нужно передать сколько добавить времени. Варианты ввода 'time':
    - Hours: Добавит час
    - day: Добавит один день
    - week: Добавит неделю на выполнения Task
    - month: Добавит месяц на выполнение Task
    :param id: int - идентификатор Task
    :param time: str - варианты ввода уже расписаны
    :return: Вернет True, если задача успешно отредактирована, либо False, если в процессе редкатирования возникли
             какие либо ошибки, из-за которых задача не может быть изменена.
    """
    pass
