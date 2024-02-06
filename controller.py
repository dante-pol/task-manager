from model.core import TaskManager, WebPresenter
import eel


@eel.expose
def get_one_task(id: int) -> str or bool:
    """
    Вернет Task по ID, формат возврата <!--надо дописать--!>, тип данных str
    :param id: int - идентификатор Task
    :return: str - Task, в случаи ошибки - вернет False
    """
    return WebPresenter.get_task(id)


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
    result = TaskManager.create_task(descript, start_time, deadline, status=is_done)
    last_task = TaskManager.get_count() - 1
    return result if not result else get_one_task(last_task)



@eel.expose
def remove_task(id: int) -> bool:
    """
    Удаляет указанный пользователем Task
    :param id: int - идентификатор Task
    :return: Вернет True, если задача успешно удалена, либо False, если в процессе удаления возникли какие либо ошибки,
             из-за которых задача не может быть удалена.
    """
    return TaskManager.delete_task(id)


@eel.expose
def switch_status(id: int) -> str or bool:
    """
    Меняет статус выполнения Task на противоположный. Вернет обновленную информацию о Task, формат возврата
    <!--надо дописать--!>, тип данных str
    :param id: int - идентификатор Task
    :return: str - Task, в случаи ошибки - вернет False
    """
    TaskManager.set_status_task(id)
    return get_one_task(id)


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
    return TaskManager.set_date_done(id, time)
