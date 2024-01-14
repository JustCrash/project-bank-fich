import pytest
import json
import os
from src.functions import mask_card_number, mask_account_number, format_date, print_last_5_transactions


def test_mask_card_number():
    """
    Тест функции mask_card_number.
    '1596837868705199' Входной номер карты или счёта.
    '1596 83** **** 5199' Ожидаемый замаскированный номер карты или счёта.
    """
    assert mask_card_number('MasterCard 1596837868705199') == 'MasterCard 1596 83** **** 5199'
    assert mask_card_number('Visa Platinem 1596837868705199') == 'Visa Platinem 1596 83** **** 5199'
    assert mask_card_number('Счёт 1596837868705199') == 'Счёт 1596 83** **** 5199'


def test_mask_account_number():
    """
    Тест функции mask_account_number.
    '64686473678894779589' Выходной номер карты или счёта.
    '**** **** **** **** 9589' Ожидаемый замаскированный входной номер карты или счёта.
    """
    assert mask_account_number('MasterCard 64686473678894779589') == 'MasterCard **** **** **** **** 9589'
    assert mask_account_number('Visa Platinem 64686473678894779589') == 'Visa Platinem **** **** **** **** 9589'
    assert mask_account_number('Счёт 64686473678894779589') == 'Счёт **** **** **** **** 9589'


def test_format_date():
    """
    Тест функции test_format_date.
    '2018-07-11T02:26:18.671407' Входные данные по дате.
    '11.07.2018' Ожидаемый результат, где идёт ДД.ММ.ГГГГ
    """
    assert format_date('2018-07-11T02:26:18.671407') == '11.07.2018'
    assert format_date('2019-04-04T23:20:05.206878') == '04.04.2019'


def test_print_last_5_transactions(capsys):
    """
    Тест функции print_last_5_transactions.
    В которой мы получаем последнии 5 операций пользователя по переводу средств.
    <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>
    """
    file_path = os.path.join(os.path.dirname(__file__), "../data/operations.json")
    with open(file_path, "r", encoding="utf-8") as file:
        json.load(file)

    print_last_5_transactions()

    captured = capsys.readouterr()
    expected_output = ['13.07.2019 Перевод с карты на счет',
                       'Maestro 1308 79** **** 7170 -> Счет **** **** **** **** 8612',
                       '97853.86 руб.',
                       '',
                       '',
                       '05.01.2019 Перевод со счета на счет',
                       'Счет 4636 36** **** 8409 -> Счет **** **** **** **** 8266',
                       '87941.37 руб.',
                       '',
                       '',
                       '15.07.2019 Открытие вклада',
                       'None -> Счет **** **** **** **** 2265',
                       '92688.46 USD',
                       '',
                       '',
                       '09.03.2018 Перевод организации',
                       'Счет 2640 62** **** 3262 -> Счет **** **** **** **** 1315',
                       '25780.71 руб.',
                       '',
                       '',
                       '']
    assert captured.out.split("\n") == expected_output
