import json
import os
from datetime import datetime


def mask_card_number(card_number):
    """
    Функция где мы делим номер карты на столбцы из 4 цифр
    и скрываем первые 6 и последние 4 цифры
    """
    masked_number = ''
    digit_count = 0
    for char in card_number:
        if char.isdigit():
            if digit_count % 4 == 0 and digit_count > 0:
                masked_number += ' '  # Добавляем пробел после каждых четырёх цифр
            if not card_number:
                return ""
            *payment_system, card_number = card_number.split()

            if not card_number:
                return card

            card_digits = "".join(card_number.split())
            formatted_number = (card_digits[:4] + f' {card_digits[4:6]}** **** ' +
                                card_digits[-4:])

            return " ".join(payment_system + [formatted_number])


def mask_account_number(account_number):
    masked_number = ''
    digit_count = 0
    for char in account_number:
        if char.isdigit():
            if digit_count % 4 == 0 and digit_count > 0:
                masked_number += ' '  # Добавляем пробел после каждых четырёх цифр
            if not account_number:
                return ""
            *payment_system, account_number = account_number.split()

            if not account_number:
                return card

            card_digits = "".join(account_number.split())
            formatted_number = ('**** **** **** **** ' + card_digits[-4:])

            return " ".join(payment_system + [formatted_number])


def format_date(date_str):
    """
    Функция для показа даты перевода
    с последней операции и далее
    """
    date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
    return date.strftime('%d.%m.%Y')


def print_last_5_transactions():
    """
    Функция в которой мы выводим посление 5 операций,
    которые получаем из файла ../data/operations.json
    """
    file_path = os.path.join(os.path.dirname(__file__), "../data/operations.json")
    with open(file_path, "r", encoding="utf-8") as file:
        operations = json.load(file)
    last_5_transactions = operations[-5:]
    for transaction in reversed(last_5_transactions):
        if transaction['state'] == 'EXECUTED':
            masked_number = mask_card_number(transaction.get('from', ''))
            to_masked = mask_account_number(transaction['to'])
            formatted_date = format_date(transaction['date'])
            print(f"{formatted_date} {transaction['description']}")
            print(f"{masked_number} -> {to_masked}")
            print(f"{transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}")
            print("\n")


print_last_5_transactions()
