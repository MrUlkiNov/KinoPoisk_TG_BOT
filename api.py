import requests
from pprint import pprint
from config import API_TOKEN
import json


def get_params(country: str, count: int) -> dict:
    """
    Функция принимает параметр отсеивания Страна и так же количество данных, возвращает словарь с API сервера
    """
    headers = {
        "X-API-KEY": API_TOKEN
    }
    response = requests.get(
        f"https://api.kinopoisk.dev/v1.4/movie?page=1&limit={count}&selectFields=name&selectFields"
        f"=rating&selectFields=year&selectFields=poster&selectFields=genres&selectFields"
        f"=countries&notNullFields=name&notNullFields=type&countries.name={country}", headers=headers)
    info = json.loads(response.text)
    return info


def print_info(params: dict, sort_type: int) -> None:
    """
    Функция принимает словарь данных, а так же тип сортировки и выводит отсортированный словарь
    """
    global result
    if sort_type == 1:
        result = sorted(params['docs'], key=lambda x: x['year'], reverse=True)
    elif sort_type == 2:
        result = sorted(params['docs'], key=lambda x: x['year'])
    pprint(result)

def client_window() -> None:
    """
    Основная функция, которая принимает от пользователя параметры и вызывает функции для вывода данных
    """
    sort_type = int(input("1 - low, 2 - high: "))
    country = input("Введите страну фильма: ")
    count = int(input("Сколько данных необходимо вывести? "))
    params = get_params(country, count)
    print_info(params, sort_type)

client_window()