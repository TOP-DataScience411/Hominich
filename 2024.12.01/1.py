from datetime import date, timedelta
from itertools import cycle

def is_in_vacation(check_date):
    """
    Функция проверяет существует ли глобальная переменная 'vacations' в глобальном пространстве имён.
    Возвращает периоды, которые должны быть исключены из графика.
    """
    global_vacations = globals().get('vacations', [])
    return any(
        start <= check_date < start + duration
        for start, duration in global_vacations
    )

def schedule(start_date, first_weekday, *weekdays, total_days, date_format='%d/%m/%Y'):
    """
    Данная функция предназначена для расчёта дат еженедельно повторяющихся событий.
    Функция принимает обязательным аргументом дату первого мероприятия в графике, обязательным аргументом один и более номеров дней недели, далее обязательным аргументом общее количество занятий, и необязательным аргументом формат строкового представления генерируемых дат.
    Дата первого мероприятия должна быть строго позиционным аргументом, передаётся в виде объекта datetime.date
    Первый номер дня недели должен быть строго позиционным аргументом. Последующие номера дней недели должны быть произвольным кортежем позиционных аргументов. Передаются в виде объектов int.
    Номера дней недели обозначают, какие дни каждой недели должны войти в график.
    Используется система нумерации ISO: 1 — понедельник, 2 — вторник, ...
    Общее количество занятий должно быть строго ключевым аргументов, передаётся в виде объекта int
    Формат строкового представления дат должен быть строго ключевым аргументом, передаётся в виде объекта str, значение по умолчанию '%d/%m/%Y'
    """
    all_weekdays = sorted((first_weekday,) + weekdays)

    schedule_dates = []
    current_date = start_date
    weekdays_cycle = cycle(all_weekdays)

    while len(schedule_dates) < total_days:
        target_weekday = next(weekdays_cycle)
        while current_date.isoweekday() != target_weekday:
            current_date += timedelta(days=1)

        if not is_in_vacation(current_date):
            schedule_dates.append(current_date.strftime(date_format))

        current_date += timedelta(days=1)

    return schedule_dates

# python3 -i 1.py
# >>> vacations = [(date(2023, 5, 1), timedelta(weeks=1)), (date(2023, 7, 17), timedelta(weeks=1))]
# >>> py321 = schedule(date(2023, 4, 1), 6, 7, total_days=70)
# >>> len(py321)
# 70
# >>> py321[28:32]
# ['15/07/2023', '16/07/2023', '29/07/2023', '30/07/2023']
# >>>
