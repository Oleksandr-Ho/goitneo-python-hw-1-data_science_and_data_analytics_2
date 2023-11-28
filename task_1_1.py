from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Підготовка Даних
    birthday_dict = defaultdict(list)
    
    # Отримання Поточної Дати
    # today = datetime.today().date()
    today = datetime(2023, 11, 29).date()

    # Перебір Користувачів
    for user in users:
        # Конвертація Дати
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        # Оцінка Дати на Цей Рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Порівняння з Поточною Датою
        delta_days = (birthday_this_year - today).days

        # Визначення Дня Тижня та Перенос на Понеділок
        if delta_days < 7:
            day_of_week = (today + timedelta(days=delta_days)).strftime('%A')
            if day_of_week in ['Saturday', 'Sunday']:
                day_of_week = 'Monday'
            birthday_dict[day_of_week].append(name)
        else:
            continue

    # Виведення Результату
    for day, names in birthday_dict.items():
        print(f"{day}: {', '.join(names)}")
